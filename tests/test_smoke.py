from traceable_agentic_rag.config import Settings, get_settings


def test_settings_loads() -> None:
    settings = get_settings()
    assert isinstance(settings, Settings)
