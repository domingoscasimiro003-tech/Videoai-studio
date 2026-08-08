def preparar_prompt(prompt: str) -> str:
    return (
        "Create a cinematic high quality video. "
        "The scene should be visually coherent and detailed. "
        f"Description: {prompt}"
    )
