
import unittest
from unittest.mock import patch, MagicMock

from main import generate_draft, improve_draft


class TestFeedbackAgent(unittest.TestCase):

    @patch.dict("os.environ", {"GROQ_API_KEY": "test-key"})
    @patch("main.OpenAI")
    def test_generate_draft(self, mock_openai):
        mock_client = MagicMock()
        mock_openai.return_value = mock_client

        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Original draft"
        mock_client.chat.completions.create.return_value = mock_response

        result = generate_draft("Write a leave email")

        self.assertEqual(result, "Original draft")
        mock_client.chat.completions.create.assert_called_once()

    @patch.dict("os.environ", {"GROQ_API_KEY": "test-key"})
    @patch("main.OpenAI")
    def test_improve_draft(self, mock_openai):
        mock_client = MagicMock()
        mock_openai.return_value = mock_client

        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Improved draft"
        mock_client.chat.completions.create.return_value = mock_response

        result = improve_draft(
            "Original draft",
            "Make it shorter"
        )

        self.assertEqual(result, "Improved draft")
        mock_client.chat.completions.create.assert_called_once()

    def test_improve_draft_rejects_empty_original(self):
        with self.assertRaises(ValueError):
            improve_draft("", "Make it shorter")

    def test_improve_draft_rejects_empty_feedback(self):
        with self.assertRaises(ValueError):
            improve_draft("Original draft", "  ")


if __name__ == "__main__":
    unittest.main()
