from groq.cloud.core import Models


class TestCoreModels:
    modelmanager = Models()

    def test_list_models(self):
        models = self.modelmanager.list_models()
        # TODO: fix for multiple models
        assert models.id == "llama2-70b-4096"
