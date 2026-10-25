
import streamlit as st
from main import generate_draft, improve_draft

st.set_page_config(
    page_title="Feedback-in-the-Loop Agent",
    page_icon="🔄",
    layout="centered"
)

st.title("🔄 Feedback-in-the-Loop Agent")
st.write(
    "Generate a draft, provide feedback, and let AI improve "
    "the result step by step."
)

# Initialize application state
if "original_draft" not in st.session_state:
    st.session_state.original_draft = ""

if "current_draft" not in st.session_state:
    st.session_state.current_draft = ""

if "feedback_history" not in st.session_state:
    st.session_state.feedback_history = []

# Section 1: User request
st.header("1. Describe what you want")

user_request = st.text_area(
    "Your writing request",
    placeholder="Example: Write a polite email requesting one day of leave.",
    height=120
)

if st.button("Generate First Draft", type="primary"):
    if not user_request.strip():
        st.warning("Please enter a writing request first.")
    else:
        try:
            with st.spinner("Generating the first draft..."):
                draft = generate_draft(user_request.strip())

            st.session_state.original_draft = draft
            st.session_state.current_draft = draft
            st.session_state.feedback_history = []
            st.success("First draft generated successfully!")

        except Exception as error:
            st.error(f"Could not generate the draft: {error}")

# Section 2: Review the current draft
if st.session_state.current_draft:
    st.header("2. Review and edit the draft")

    edited_draft = st.text_area(
        "Current draft",
        value=st.session_state.current_draft,
        height=300,
        key="draft_editor"
    )

    # Section 3: Human feedback
    st.header("3. Give feedback")

    feedback = st.text_area(
        "How should the draft be improved?",
        placeholder=(
            "Example: Make it shorter, more polite, "
            "and use simple English."
        ),
        height=100,
        key="feedback_input"
    )

    if st.button("Improve Draft", type="primary"):
        if not edited_draft.strip():
            st.warning("The draft cannot be empty.")
        elif not feedback.strip():
            st.warning("Please enter feedback before improving the draft.")
        else:
            try:
                with st.spinner("Improving the draft using your feedback..."):
                    revised_draft = improve_draft(
                        edited_draft.strip(),
                        feedback.strip()
                    )

                st.session_state.current_draft = revised_draft
                st.session_state.feedback_history.append(
                    {
                        "feedback": feedback.strip(),
                        "draft": revised_draft
                    }
                )

                # Clear widget values so the revised draft and
                # an empty feedback field appear after rerunning.
                st.session_state.pop("draft_editor", None)
                st.session_state.pop("feedback_input", None)

                st.rerun()

            except Exception as error:
                st.error(f"Could not improve the draft: {error}")

    # Section 4: Download the latest draft
    st.header("4. Download your draft")

    st.download_button(
        label="Download Current Draft",
        data=st.session_state.current_draft,
        file_name="improved_draft.txt",
        mime="text/plain"
    )

    # Section 5: Show feedback history
    if st.session_state.feedback_history:
        st.header("Feedback History")

        for index, item in enumerate(
            st.session_state.feedback_history, start=1
        ):
            with st.expander(f"Revision {index}"):
                st.write("**Human feedback:**")
                st.write(item["feedback"])
                st.write("**Revised draft:**")
                st.write(item["draft"])

    with st.expander("View the original draft"):
        st.write(st.session_state.original_draft)

st.caption(
    "Human feedback guides each revision. Always review AI-generated "
    "content before using it."
)
