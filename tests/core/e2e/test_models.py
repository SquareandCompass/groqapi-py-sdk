from groq.cloud.core import Models


class TestCoreModels:
    modelmanager = Models()

    def test_list_models(self):
        models = self.modelmanager.list_models()
        contains_llama_70b = False

        # TODO: perhaps a more robust check than this
        for model in models:
            if model.id == "llama2-70b-4096":
                contains_llama_70b = True
        assert contains_llama_70b
