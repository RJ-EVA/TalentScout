from llm_service import screen_resume


def get_candidate_fields():
    return [
        ("full_name", "Full Name"),
        ("email", "Email Address"),
        ("position", "Desired Role"),
    ]


def run_resume_screening(resume_text: str, candidate: dict) -> str:
    return screen_resume(
        resume_text=resume_text,
        role=candidate["position"],
    )
