# doc2kg

---

curl -X POST "https://--modal-.modal.run" -F "file=@/Users/<user>/Downloads/LLM-Training-and-Applications-LLMs-are-trained-on-a-corpus-large-volume-of-text-data.jpg""


---

```
{
  "ai_kg": {
    "name": "language_models_knowledge_graph",
    "nodes": [
      {
        "id": "1",
        "label": "Large Language Models",
        "properties": {
          "topic": "natural language processing",
          "technology": "deep learning"
        }
      },
      {
        "id": "2",
        "label": "Reinforcement Learning",
        "properties": {
          "field": "machine learning",
          "related_to": "human feedback"
        }
      },
      {
        "id": "3",
        "label": "Human Feedback",
        "properties": {
          "type": "feedback mechanism"
        }
      },
      {
        "id": "4",
        "label": "Alignment",
        "properties": {
          "goal": "model alignment with human values"
        }
      },
      {
        "id": "5",
        "label": "Sentiment Analysis",
        "properties": {
          "application": "text processing"
        }
      },
      {
        "id": "6",
        "label": "Text Summarization",
        "properties": {
          "application": "text processing"
        }
      },
      {
        "id": "7",
        "label": "Language Translation",
        "properties": {
          "application": "text processing"
        }
      },
      {
        "id": "8",
        "label": "Conversational AI Interface",
        "properties": {
          "type": "user interaction technology"
        }
      }
    ],
    "edges": [
      {
        "source": "1",
        "target": "2",
        "label": "utilizes"
      },
      {
        "source": "2",
        "target": "3",
        "label": "based on"
      },
      {
        "source": "3",
        "target": "4",
        "label": "promotes"
      },
      {
        "source": "1",
        "target": "5",
        "label": "enables"
      },
      {
        "source": "1",
        "target": "6",
        "label": "enables"
      },
      {
        "source": "1",
        "target": "7",
        "label": "enables"
      },
      {
        "source": "1",
        "target": "8",
        "label": "interacts_with"
      }
    ]
  }
}
```
