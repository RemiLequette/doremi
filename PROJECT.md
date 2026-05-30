# doremi

## Purpose

Assistant domotique vocal comprenant le langage naturel en français pour contrôler
des appareils et services à la maison.

## Objectifs

- Comprendre le langage naturel (oral et écrit) en français.
- Identifier des domaines d'activité (musique, lumière, sécurité, température, vidéo)
  à partir de mots-clés ou de demandes simples.
- Traduire les commandes vocales en instructions pour des outils (Home Assistant, Kodi, etc.)
  selon des règles prédéfinies.
- Tester en cloud avant de déployer en local.

## Domaines couverts

musique | lumière | sécurité | température | vidéo

## Structure

- `Claude.md` — Instructions pour les sessions Claude
- `PROJECT.md` — Ce fichier : métadonnées et objectifs du projet
- `README.md` — Navigation pour les humains
- `docs/` — Documentation technique (architecture, outils, feuille de route)

## Phases

**Phase 1 — Cloud** : tests avec APIs gratuites (Hugging Face, Mistral AI, Home Assistant)

**Phase 2 — Local** : déploiement via Ollama sur mini-PC après validation des performances

---

## Audit

Pour auditer la conformité de ce projet aux bonnes pratiques :

1. Lire : `C:\Users\RemiLequette\Development\projects\claude-knowledge\guides\audit-process.md`
2. Vérifier contre : `C:\Users\RemiLequette\Development\projects\claude-knowledge\guides\Claude.ai-best-practices.md`

---

## Keywords
doremi, domotique, vocal, LLM, home-assistant, objectifs, projet
