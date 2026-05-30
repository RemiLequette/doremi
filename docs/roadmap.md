# Feuille de route

## Table des matières

- [Vue d'ensemble](#vue-densemble)
- [Etapes](#etapes)
- [Conseils et bonnes pratiques](#conseils-et-bonnes-pratiques)
- [Keywords](#keywords)

---

## Vue d'ensemble [↑](#table-des-matières)

Durée totale estimée : **7–12 jours**

Phase 1 (Cloud) → valider précision et latence → Phase 2 (Local via Ollama)

---

## Etapes [↑](#table-des-matières)

| # | Objectif | Outils | Durée estimée |
|---|----------|--------|---------------|
| 1 | Tester la reconnaissance vocale | Whisper (Hugging Face) | 1–2 jours |
| 2 | Tester le LLM | Mistral-7B / Phi-3 (Hugging Face) | 2–3 jours |
| 3 | Valider classification et traduction JSON | Prompts optimisés | 1–2 jours |
| 4 | Intégrer avec la domotique | Home Assistant API | 2–3 jours |
| 5 | Passer en local | Ollama + Whisper + Phi-3 | 1–2 jours |

---

## Conseils et bonnes pratiques [↑](#table-des-matières)

- **Prompts** : être précis (ex. "Réponds toujours en JSON").
- **Latence** : utiliser des modèles légers (ex. phi-3-mini).
- **Sécurité** : sécuriser le réseau (VPN pour accéder à Home Assistant à distance).
- **Evolutivité** : ajouter des domaines et des règles au fur et à mesure.

---

## Keywords
roadmap, feuille-de-route, etapes, planning, phase1, phase2, cloud, local
