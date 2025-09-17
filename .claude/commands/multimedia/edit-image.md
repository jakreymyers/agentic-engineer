---
name: Edit Image
allowed-tools: Bash, Read
description: Edit existing images via Replicate using direct curl API calls
---

# Edit Image

Edit existing images based on provided edit prompts using Replicate's API directly via curl.

## Variables

DROPPED_FILE_PATH: $1
DROPPED_FILE_PATH_ARCHIVE: ./agentic-engineer/docs/images/drop-zone/edit-image/archive/<date_time>/
IMAGE_OUTPUT_DIR: ./agentic-engineer/docs/images/drop-zone/edit-image/<date_time>/
- This is the directory where all images will be saved
- The date_time is the current date and time in the format DD-MMM-YYYY_HH-MM-SS
MODEL: google/nano-banana
API_ENDPOINT: https://api.replicate.com/v1/models/google/nano-banana/predictions

## Workflow
- Check these prerequisites and STOP immediately if you don't have them:
  - REPLICATE_API_TOKEN must be exported in the environment
  - Requires base64 command for inline image encoding
- Note: REPLICATE_API_TOKEN will be available, don't search for it and NEVER read the .env file directly.
  - IMPORTANT: If for some reason you run into issues with authentication, abort immediately - do not continue with any image processing. Mention that the REPLICATE_API_TOKEN might be missing.
- First, read `DROPPED_FILE_PATH`.
- Create output directory: `IMAGE_OUTPUT_DIR/‹date_time>/`
- IMPORTANT: For every image edit detailed in the `DROPPED_FILE_PATH` do the following:

<image-loop>
  - Extract the source image path and edit prompt from the dropped file
  - Use curl with inline base64 encoding to send image directly to Replicate API:
    ```bash
    curl -s -X POST \
      -H "Authorization: Bearer $REPLICATE_APA_TOKEN" \
      -H "Content-Type: application/json" \
      -H "Prefer: wait" \
      -d '{
        "input": {
          "prompt": "YOUR_EDIT_PROMPT_HERE",
          "image_input": ["data:image/jpeg;base64,'$(base64 -i /path/to/source/image-jpg)'"],
          "output_format": "jpg"
        }
      }' \
      https://api.replicate.com/v1/models/google/nano-banana/predictions
  ```

  - IMPORTANT: Replace `YOUR_EDIT_PROMPT_HERE` with the actual edit instruction
  - IMPORTANT: Replace `/path/to/source/image-jpg` with the actual source image path which should be detailed in the `DROPPED_FILE_PATH`
  - IMPORTANT: The base64 encoding happens inline using `$(base64 -i /path/to/image.jpg)`
  - Parse JSON response to extract the `output` URL field for the generated image
    - Response format: `{"id":"...", "output":"https://replicate.delivery/...jpg", "status":"succeeded"}`
    - Extract URL with `jq -r '.output'`
  - Save the executed edit prompts to `IMAGE_OUTPUT_DIR/<date_time>/edit_prompt_<concise_name_based_on_prompt>.txt`
    - Include both the source image path and the exact edit prompt that was executed
  - Download the edited image from the output URL: `curl -o IMAGE_OUTPUT_DIR/<date_time>/<MODEL_NAME_underscore_separated>_edited_<concise_name_based_on_prompt>.jpg "OUTPUT_URL"`
  - Display:
    - Source image path
    - Edit prompt used
    - Generation time (if available in response)
    - File size of downloaded image
    - Full path to saved edited image
    - Replicate output URL for reference
</image-loop>

- After all images are edited, copy all original source images to the output directory for reference:
  - For each source image that was processed, copy it with "original_" prefix
  - Example: `cp /path/to/cat.jpg IMAGE_OUTPUT_DIR/<date_time>/original_cat.jpg`
  - This allows easy before/after comparison in the same directory
- After copying originals, open the output directory: `open IMAGE_OUTPUT_DIR/<date_time>/`
- When you finish editing images, move the `DROPPED_FILE_PATH` into a `DROPPED_FILE_PATH_ARCHIVE` directory