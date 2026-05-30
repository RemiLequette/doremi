# Architecture et Outils

## Table des matières

- [Pipeline complet](#pipeline-complet)
- [Phase 1 — Cloud](#phase-1--cloud)
- [Phase 2 — Local](#phase-2--local)
- [Matériel recommandé](#matériel-recommandé)
- [Exemples de code](#exemples-de-code)
- [Points à valider pendant les tests](#points-à-valider-pendant-les-tests)
- [Ressources](#ressources)
- [Keywords](#keywords)

---

## Pipeline complet [↑](#table-des-matières)

```
Audio → Speech-to-Text → LLM (classification + JSON) → API domotique
```

Objectif de latence totale : < 5 secondes.

---

## Phase 1 — Cloud [↑](#table-des-matières)

### Speech-to-Text

| Outil | Modèle | Avantages | Quota gratuit |
|-------|--------|-----------|---------------|
| Hugging Face | whisper-1 | Open source, français | 500 req/mois |
| Google Speech-to-Text | — | Excellente précision | 60 min/mois |
| AssemblyAI | — | API simple | 5h/mois |

**Recommandation :** Hugging Face (Whisper) — gratuit, open source.

### LLM

| Outil | Modèle | Avantages | Quota gratuit |
|-------|--------|-----------|---------------|
| Hugging Face | mistral-7b, phi-3 | Open source | 500 req/mois |
| Mistral AI | mistral-tiny, mistral-small | Optimisé français | 1M tokens/mois |
| Google Vertex AI | gemini-1.5-flash | Bon français | 1M tokens/mois |

**Recommandation :** Mistral AI (quota généreux) ou Hugging Face (phi-3/mistral-7b).

### Exécution des instructions

| Outil | API | Usage |
|-------|-----|-------|
| Home Assistant | REST API | Lumières, température, sécurité |
| Kodi | JSON-RPC | Contrôle multimédia |
| IFTTT/Webhooks | Webhooks | Simulation rapide pour tests |

**Recommandation :** Home Assistant si déjà installé, sinon IFTTT pour les premiers tests.

---

## Phase 2 — Local [↑](#table-des-matières)

Tous les composants tournent via **Ollama** sur un mini-PC local.

| Composant | Outil |
|-----------|-------|
| Speech-to-Text | Whisper (Ollama) |
| LLM | Phi-3 ou Mistral-7B (Ollama) |
| Exécution | Home Assistant |

### Installation Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull phi3
ollama pull whisper
```

### Lancer les modèles

```bash
ollama run phi3
ollama run whisper
```

---

## Matériel recommandé [↑](#table-des-matières)

| Composant | Recommandation | Coût estimé |
|-----------|----------------|-------------|
| Ordinateur | Mini-PC avec GPU (ex. NVIDIA RTX 3060) ou Raspberry Pi 5 | 500–1500 € |
| Microphone | Blue Yeti ou ReSpeaker | 50–150 € |
| Stockage | SSD 500 Go | 50–100 € |

---

## Exemples de code [↑](#table-des-matières)

### Speech-to-Text — Whisper via Hugging Face

```python
import requests

def speech_to_text(audio_file, hf_token):
    with open(audio_file, "rb") as f:
        response = requests.post(
            "https://api-inference.huggingface.co/models/openai/whisper-1",
            headers={"Authorization": f"Bearer {hf_token}"},
            files={"file": f}
        )
    return response.json()["text"]
```

### LLM — Mistral-7B via Hugging Face

```python
import json

def process_command(text, hf_token):
    prompt = f"""
    Tu es un assistant domotique. Classifie la demande suivante dans un domaine parmi :
    [musique, video, lumiere, securite, temperature].
    Puis traduis-la en une instruction JSON pour l'outil correspondant.
    Demande : "{text}"
    Reponse attendue (format JSON) :
    """
    response = requests.post(
        "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2",
        headers={"Authorization": f"Bearer {hf_token}"},
        json={"inputs": prompt}
    )
    generated_text = response.json()[0]["generated_text"]
    start = generated_text.find("{")
    end = generated_text.rfind("}") + 1
    return json.loads(generated_text[start:end])
```

### Exécution — Home Assistant

```python
def execute_instructions(instructions, ha_token, ha_ip):
    for instruction in instructions:
        if instruction["outil"] == "home_assistant":
            action = instruction["action"]
            cible = instruction["cible"]
            if action == "allumer":
                requests.post(
                    f"http://{ha_ip}/api/services/light/turn_on",
                    headers={"Authorization": f"Bearer {ha_token}", "Content-Type": "application/json"},
                    json={"entity_id": cible}
                )
```

### Workflow local — Ollama

```python
def speech_to_text_local(audio_file):
    with open(audio_file, "rb") as f:
        response = requests.post(
            "http://localhost:11434/api/generate",
            data=f.read(),
            headers={"Content-Type": "audio/wav"},
            params={"model": "whisper"}
        )
    return response.json()["response"]

def process_command_local(text):
    prompt = f"""
    Tu es un assistant domotique. Classifie la demande dans un domaine parmi :
    [musique, video, lumiere, securite, temperature].
    Puis traduis-la en instruction JSON.
    Demande : "{text}"
    Reponse attendue (format JSON) :
    """
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "phi3", "prompt": prompt, "stream": False}
    )
    return json.loads(response.json()["response"])
```

---

## Points à valider pendant les tests [↑](#table-des-matières)

1. **Reconnaissance vocale** — précision sur phrases courtes, accents, bruit de fond.
2. **Classification des domaines** — tester des phrases ambiguës (ex. "Lance Netflix" → vidéo).
3. **Traduction en JSON** — vérifier validité du JSON, tester commandes complexes (ex. "Allume la lumière et lance ma playlist jazz").
4. **Latence** — mesurer le temps total, objectif < 5 secondes.
5. **Intégration API** — compatibilité des instructions JSON avec Home Assistant / Kodi.

---

## Ressources [↑](#table-des-matières)

- Hugging Face Inference API : https://huggingface.co/docs/api-inference
- Mistral AI API : https://docs.mistral.ai
- Home Assistant REST API : https://developers.home-assistant.io/docs/api/rest
- Ollama : https://ollama.com/docs

---

## Keywords
architecture, outils, speech-to-text, whisper, mistral, phi-3, home-assistant, kodi, ollama, cloud, local, pipeline, code, exemples
