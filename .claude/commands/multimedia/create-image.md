---
name: Create Image
allowed-tools: Bash, mcp__replicate__create_models_predictions, mcp__replicate__get_predictions, Write 
description: Generate image(s) via Replicate
argument-hint: [image generatton prompt] [number of images]
---

# Create Image

Generates image(s) based on the provided prompt using Replicate MCP server.

## Variables

IMAGE_GENERATION-PROMPT: $1
NUMBER_OF_IMAGES: $2 (or 3 if not provided)
IMAGE_OUTPUT_DIR: ./agentic-engineer/docs/images/drop-zone/create-image/<date_time>/
    - This is the directory where all images will be saved
    - The date_time is the current date and time in the format DD-MMM-YYYY_HH-MM-SS
MODEL: google/nano-banana
ASPECT_RATIO: 16:9

## Workflow
- First, check your system prompt to make sure you have `mcp__replicate__create_models_predictions` and `mcp__replicate__get_predictions` available. If not, STOP immediately and ask the user to add them.
- Then check to see if `IMAGE_GENERATION_PROMPT` is provided. If not, STOP immediately and ask the user to provide it.
- Take note of `IMAGE_GENERATION_PROMPT` and `NUMBER_OF_IMAGES`.
- Get the current <date_time> by running `date +&Y-%m-%d_%H-eM-%5`
- Echo the <date_time>, use this exact value for the output directory name
- Create output directory: `IMAGE_OUTPUT _DIR/<date_time>/`
- IMPORTANT: Then generate `NUMBER_OF_IMAGES` images using the `IMAGE_GENERATION_PROMPT` following the `image-loop` below.

<image-loop>
  - Use `mcp__replicate__create_models_predictions` with the MODEL specified above
  - Pass image prompt as the prompt input
  - Use ASPECT_RATIO for the image dimensions
  - Wait for completion by polling `mcp__replicate__get_predictions`
  - Save the executed prompts to `IMAGE_OUTPUT_DIR/<date_time>/image_prompt_<concise_name_based_on_prompt>.txt`
    - Use the exact prompt that was executed in the `mcp__replicate__create_models_predictions` call
  - Download the image: `IMAGE_OUTPUT_DIR/<date_time>/<MODEL_NAME_underscore_separated>_<concise_name_based_on_prompt>.jpg`
</image-loop>

- After all images are generated, open the output directory: `open IMAGE_OUTPUT_DIR/<date_time>/`

## Report

- Report the total number of images generated
- Report the full path to the output directory