from groq.cloud.core import Completion
from groq.cloud.core.exceptions import ModelUnavailableError, InvalidArgumentError


class TestCoreCompletion:
    def test_completion(self):
        compl = Completion()
        prompt = "print the number 7"
        response, id, stats = compl.send_prompt(
            "llama2-70b-4096",
            user_prompt=prompt,
            system_prompt="only respond with the number 7",
        )
        assert response == "Sure! Here is the number 7: 7"

    def test_completion_bad_model(self):
        compl = Completion()
        prompt = "print the number 7"
        try:
            response, id, stats = compl.send_prompt(
                "haxor-1337",
                user_prompt=prompt,
                system_prompt="only respond with the number 7",
            )
        except Exception as e:
            assert type(e) is InvalidArgumentError
            return

        assert False

    def test_completion_streaming(self):
        compl = Completion()
        prompt = "print the number 7"
        response = compl.send_prompt(
            "llama2-70b-4096",
            user_prompt=prompt,
            system_prompt="only respond with the number 7",
            streaming=True,
        )
        # needed to skip nondet request id
        next(response)
        assert str(next(response)) == 'content: "Sure"\n'

    # This shoudl work, something about how grpc exceptions are raised?
    # def test_completion_streaming_bad_model(self):
    #     compl = Completion()
    #     prompt = "print the number 7"
    #     try:
    #         response, id, stats = compl.send_prompt(
    #             "haxor-1337",
    #             user_prompt=prompt,
    #             system_prompt="only respond with the number 7",
    #             streaming=True,
    #         )
    #     except Exception as e:
    #         assert type(e) is InvalidArgumentError
    #         return

    #     assert False
