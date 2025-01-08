import modal

from fastapi import UploadFile, File, HTTPException
from fastapi.responses import JSONResponse


# Define the Docker image
docker_image = modal.Image.debian_slim().pip_install("fastapi", "requests", "docling", "openai")

# Create a Modal app
app = modal.App("modal-doc2kg")

@app.function(
    image=docker_image,
    gpu="any", secrets=[modal.Secret.from_dotenv()]    
)
@modal.web_endpoint(method="POST", docs=True)
async def extract_kg(file: UploadFile = File(...)):  
    import tempfile
    import os
    import json
    
    try:
        from docling.document_converter import DocumentConverter

    except ImportError:
        raise HTTPException(status_code=500, detail="docling package is not installed")
    
    if not file:  
        raise HTTPException(status_code=400, detail="No file part in the request")  
  
    if not file.filename:  
        raise HTTPException(status_code=400, detail="No file selected")  
  
    try:
        from openai import OpenAI
    
    except ImportError:
        raise HTTPException(status_code=500, detail="openai package is not installed")
    
    try:  
        # Save the uploaded file temporarily  
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:  
            contents = await file.read()  # Read the file contents asynchronously  
            temp_file.write(contents)  
            temp_file_path = temp_file.name  
  
        # Process the file using docling  
        converter = DocumentConverter()  
        result = converter.convert(temp_file_path)  
        markdown_content = result.document.export_to_markdown()  
        # set os env value for OPENAI_API_KEY
        os.environ["OPENAI_API_KEY"] = os.environ["OAI_API_KEY"]
        client = OpenAI()

        completion = client.chat.completions.create(
            model="gpt-4o-mini",#"gpt-3.5-turbo-0125",
            response_format={ "type": "json_object" },
            messages=[
                    {
                        "role": "user",
                        "content": f"""
Given this markdown content:
[markdown_content]
{markdown_content}
[/markdown_content]
"""+"""
Extract a knowledge graph from the markdown content and return it as a JSON object.

The JSON object should have the following structure:
```json
{
    "name": "your_knowledge_graph_name",
    "nodes": [
        {
            "id": "node_id",
            "label": "node_label",
            "properties": {
                "property_name": "property_value"
            }
        }
    ],
    "edges": [
        {
            "source": "source_node_id",
            "target": "target_node_id",
            "label": "edge_label"
        }
    ]
}
```
Return the knowledge graph as a JSON object.
        """
                    }
                ]
        )
        return JSONResponse(content={"ai_kg": json.loads(completion.choices[0].message.content)}) 
    except Exception as e:  
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")  
    finally:  
        # Clean up the temporary file  
        if 'temp_file_path' in locals() and os.path.exists(temp_file_path):  
            os.unlink(temp_file_path)  
if __name__ == "__main__":
    with modal.enable_remote_debugging():
        with app.run():
            extract_kg.remote()
