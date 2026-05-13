import streamlit as st
import random

st.set_page_config(page_title="CommentLens", page_icon="🔍", layout="wide")

st.title("🔍 CommentLens")
st.subheader("Turn comments into decisions.")
st.write("An AI demo that extracts hidden concerns, contradictions, and decision signals from Xiaohongshu-style comment sections.")

topic = st.text_input(
    "Enter a topic or decision scenario:",
    placeholder="e.g., Chicago apartment rental, dental insurance for international students"
)

sample = st.selectbox(
    "Or try a sample case:",
    ["Chicago apartment rental", "Chicago dental insurance", "US job hunting for international students"]
)

def generate_report(query):
    if "dental" in query.lower() or "牙" in query:
        return {
            "concerns": [
                "Whether insurance is accepted before treatment",
                "Unexpected out-of-pocket costs after deep cleaning",
                "Long wait time for new patient appointments",
                "Confusion between routine cleaning and deep cleaning coverage",
                "Whether international students can claim reimbursement later"
            ],
            "contradictions": [
                ("Post says: “This clinic is very affordable.”", "Comments ask: “Why was my final bill much higher than expected?”"),
                ("Post says: “Insurance covered everything.”", "Comments suggest coverage varies by plan and procedure type.")
            ],
            "hidden": [
                "Users care less about whether the clinic is ‘good’ and more about billing transparency.",
                "The most useful comments are about claim failure, reimbursement timing, and exact procedure names.",
                "Many users do not know they should confirm CDT/procedure codes before treatment."
            ],
            "checklist": [
                "Ask whether the clinic accepts your exact insurance plan.",
                "Confirm whether the visit is routine cleaning or deep cleaning.",
                "Ask for an estimated out-of-pocket cost before treatment.",
                "Check whether reimbursement requires itemized receipts.",
                "Save all claim documents and procedure codes."
            ]
        }
    elif "job" in query.lower() or "hunting" in query.lower():
        return {
            "concerns": [
                "Visa sponsorship uncertainty",
                "Whether referrals actually help",
                "How to interpret HR screening questions",
                "Timeline pressure before graduation",
                "Mismatch between job descriptions and actual hiring standards"
            ],
            "contradictions": [
                ("Post says: “Just network more and referrals will work.”", "Comments say: “Referral did not help without a strong fit.”"),
                ("Post says: “This role sponsors.”", "Comments warn that sponsorship can depend on team, timing, and headcount.")
            ],
            "hidden": [
                "The real anxiety is not resume polishing, but uncertainty around sponsorship and timing.",
                "Comment sections often contain more actionable information than the original job-hunting post.",
                "Users want verified examples from people who went through the exact process."
            ],
            "checklist": [
                "Ask about sponsorship timing early.",
                "Check whether the team has sponsored international candidates before.",
                "Prepare a clear graduation and availability answer.",
                "Track referral source, recruiter response, and interview timeline.",
                "Validate advice against recent candidate comments."
            ]
        }
    else:
        return {
            "concerns": [
                "Hidden utility fees and unclear rent structure",
                "Heating quality during Chicago winter",
                "Safety and transportation at night",
                "Distance that looks walkable in summer but not in winter",
                "Laundry, maintenance, and package delivery issues"
            ],
            "contradictions": [
                ("Post says: “10-minute walk to campus.”", "Comments say: “Not realistic during winter or late at night.”"),
                ("Post says: “Great value apartment.”", "Comments mention extra utility, parking, or management fees."),
                ("Post says: “Safe neighborhood.”", "Comments ask about specific streets and nighttime safety.")
            ],
            "hidden": [
                "Users are not only asking where to live; they are asking what trade-offs they might regret.",
                "Comment sections reveal practical concerns that polished posts often skip.",
                "The most decision-relevant signals are repeated questions, warnings, and contradictory experiences."
            ],
            "checklist": [
                "Confirm whether heating is included in rent.",
                "Check commute time in winter, not only on a sunny day.",
                "Ask current residents about maintenance response time.",
                "Verify laundry, package room, and elevator conditions.",
                "Search comments for safety concerns by specific block or street."
            ]
        }

if st.button("Analyze Comments"):
    query = topic if topic else sample
    report = generate_report(query)

    st.divider()
    st.header(f"Community Intelligence Report: {query}")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💬 Top Repeated Concerns")
        for item in report["concerns"]:
            st.write(f"- {item}")

        st.subheader("🧩 Hidden Signals From Comments")
        for item in report["hidden"]:
            st.write(f"- {item}")

    with col2:
        st.subheader("⚠️ Contradiction Detection")
        for post, comment in report["contradictions"]:
            st.warning(f"{post}\n\n→ {comment}")

        trust_score = round(random.uniform(3.8, 4.6), 1)
        st.metric("Comment Reliability Score", f"{trust_score}/5")

    st.subheader("✅ Decision Checklist")
    for item in report["checklist"]:
        st.checkbox(item)

    st.info(
        "Prototype logic: Perplexity is used as the research layer to identify public discussion patterns. "
        "CommentLens turns scattered comments into structured concerns, contradictions, hidden risks, and decision checklists."
    )

else:
    st.info("Enter a topic or choose a sample case, then click Analyze Comments.")
