
from main import generate_draft, improve_draft


def main():
    # Step 1: Generate the original draft
    request = (
        "Write a polite email requesting one day of leave "
        "from my manager. Do not invent a reason for the leave "
        "or claim that work has been completed. Use placeholders "
        "for missing information."
    )

    print("\n" + "=" * 50)
    print("STEP 1: GENERATE ORIGINAL DRAFT")
    print("=" * 50)

    try:
        draft = generate_draft(request)
        print("\nORIGINAL DRAFT:\n")
        print(draft)

        # Step 2: Get the first round of human feedback
        print("\n" + "=" * 50)
        print("STEP 2: FIRST ROUND OF HUMAN FEEDBACK")
        print("=" * 50)

        feedback_1 = input(
            "\nEnter your feedback for the first revision: "
        ).strip()

        if not feedback_1:
            print("Feedback cannot be empty. Please try again.")
            return

        # Step 3: Generate the first revision
        improved_draft_1 = improve_draft(draft, feedback_1)

        print("\nFIRST REVISION:\n")
        print(improved_draft_1)

        # Step 4: Get the second round of human feedback
        print("\n" + "=" * 50)
        print("STEP 3: SECOND ROUND OF HUMAN FEEDBACK")
        print("=" * 50)

        feedback_2 = input(
            "\nEnter your feedback for the second revision: "
        ).strip()

        if not feedback_2:
            print("Feedback cannot be empty. Please try again.")
            return

        # Step 5: Generate the second revision
        improved_draft_2 = improve_draft(
            improved_draft_1,
            feedback_2
        )

        print("\n" + "=" * 50)
        print("FINAL IMPROVED DRAFT")
        print("=" * 50)
        print(improved_draft_2)

        print("\nFeedback loop completed successfully!")

    except Exception as error:
        print(f"\nAn error occurred: {error}")


if __name__ == "__main__":
    main()
