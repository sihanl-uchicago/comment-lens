import streamlit as st
import random

st.set_page_config(
    page_title="CommentLens",
    page_icon="🔍",
    layout="wide"
)

# -----------------------------
# Smart Query Router
# -----------------------------
def classify_query(query):
    q = query.lower()

    categories = {
        "Travel": ["杭州", "上海", "北京", "东京", "巴黎", "旅行", "旅游", "酒店", "景点", "city", "trip", "travel", "hotel"],
        "Beauty": ["面霜", "口红", "护肤", "粉底", "防晒", "敏感肌", "skincare", "makeup", "beauty", "serum"],
        "Food": ["咖啡", "餐厅", "火锅", "奶茶", "brunch", "restaurant", "coffee", "food", "dessert"],
        "Fashion": ["lululemon", "aritzia", "穿搭", "衣服", "包", "leggings", "fashion", "outfit"],
        "Education": ["mba", "留学", "申请", "学校", "大学", "graduate", "school", "career"],
        "Tech": ["ai", "chatgpt", "app", "软件", "产品", "tech", "tool", "startup"],
    }

    for category, keywords in categories.items():
        if any(k in q for k in keywords):
            return category

    return "Lifestyle"


# -----------------------------
# Demo Insight Generator
# -----------------------------
def generate_insights(query, category):
    templates = {
        "Travel": {
            "sentiment": (72, 18, 10),
            "likes": [
                "Scenic spots and photo-friendly locations are frequently praised.",
                "Users mention strong food, cafe, and short-trip potential.",
                "Many comments frame it as a good weekend or holiday destination."
            ],
            "complaints": [
                "Crowds during holidays are the most common complaint.",
                "Transportation and itinerary planning can be tiring.",
                "Some popular spots are described as over-commercialized."
            ],
            "quotes": [
                f"“{query} is beautiful, but I would avoid peak season.”",
                f"“The hidden local spots are more interesting than the famous ones.”",
                f"“Great for photos, but planning ahead really matters.”"
            ],
            "persona": "Best for weekend travelers, couples, foodies, and photo lovers."
        },
        "Beauty": {
            "sentiment": (64, 22, 14),
            "likes": [
                "Texture, packaging, and ease of daily use are frequently mentioned.",
                "Users value visible but gradual improvement.",
                "Repeat purchase intention appears when price is reasonable."
            ],
            "complaints": [
                "Effectiveness varies by skin type.",
                "Price sensitivity is high.",
                "Some users say the product requires consistent use to see results."
            ],
            "quotes": [
                f"“{query} feels nice, but it is not a miracle product.”",
                f"“I would repurchase if there is a discount.”",
                f"“It worked for me, but skin type really matters.”"
            ],
            "persona": "Best for skincare beginners, sensitive-skin users, and value-conscious buyers."
        },
        "Food": {
            "sentiment": (69, 20, 11),
            "likes": [
                "Taste, atmosphere, and social-sharing value are frequently praised.",
                "Users often recommend it for friend gatherings.",
                "Visual presentation and store vibe drive strong interest."
            ],
            "complaints": [
                "Long waiting time is a recurring issue.",
                "Some users question value for money.",
                "Experience may vary by location or time of visit."
            ],
            "quotes": [
                f"“{query} is worth trying, but go early to avoid the line.”",
                f"“The vibe is great for photos.”",
                f"“Taste is good, but the price is slightly high.”"
            ],
            "persona": "Best for foodies, friend gatherings, and social media users."
        },
        "Fashion": {
            "sentiment": (67, 21, 12),
            "likes": [
                "Design, fit, and daily wearability are frequently mentioned.",
                "Brand image creates strong purchase interest.",
                "Users like items that are easy to style."
            ],
            "complaints": [
                "Sizing can be inconsistent.",
                "Price is a major concern.",
                "Some users question durability or cost-performance."
            ],
            "quotes": [
                f"“{query} looks good, but size selection matters.”",
                f"“I like the style, but I waited for a sale.”",
                f"“Very wearable for daily outfits.”"
            ],
            "persona": "Best for young professionals, lifestyle shoppers, and trend followers."
        },
        "Education": {
            "sentiment": (61, 27, 12),
            "likes": [
                "Users care most about outcomes, career value, and peer experience.",
                "Practical application advice receives strong engagement.",
                "First-hand experience is considered more trustworthy than generic guides."
            ],
            "complaints": [
                "Cost and uncertainty are major concerns.",
                "The application process feels stressful.",
                "Information quality varies significantly across posts."
            ],
            "quotes": [
                f"“{query} is valuable, but you need to be clear about your goal.”",
                f"“The most useful posts are from people who actually went through it.”",
                f"“Cost is the biggest thing to consider.”"
            ],
            "persona": "Best for applicants, career switchers, and international students."
        },
        "Tech": {
            "sentiment": (66, 24, 10),
            "likes": [
                "Users are curious about productivity gains and practical use cases.",
                "Early adopters share detailed workflows.",
                "Clear tutorials and examples increase trust."
            ],
            "complaints": [
                "Some users are confused about setup.",
                "Trust and accuracy concerns remain.",
                "Users want more examples before paying."
            ],
            "quotes": [
                f"“{query} is useful once you know the right workflow.”",
                f"“The idea is cool, but onboarding could be better.”",
                f"“I want more examples before paying for it.”"
            ],
            "persona": "Best for students, creators, productivity users, and early adopters."
        },
        "Lifestyle": {
            "sentiment": (58, 29, 13),
            "likes": [
                "Users show broad curiosity and emotional engagement.",
                "Many posts focus on personal experience and decision-making.",
                "The topic is useful for discovering trends and consumer pain points."
            ],
            "complaints": [
                "Comments are scattered and subjective.",
                "General searches need stronger filtering.",
                "Users often disagree depending on personal preference."
            ],
            "quotes": [
                f"“{query} has mixed reviews, so I checked multiple posts.”",
                f"“The comments are more useful than the post itself.”",
                f"“It depends a lot on personal preference.”"
            ],
            "persona": "Best for trend explorers, casual researchers, and consumer insight users."
        }
    }

    return templates.get(category, templates["Lifestyle"])


# -----------------------------
# UI
# -----------------------------
st.title("🔍 CommentLens")
st.caption("Turn social comments into consumer insights — fast, structured, and searchable.")

st.markdown(
    """
    CommentLens helps users understand what people really say about any topic by summarizing 
    social-style comments into sentiment, likes, complaints, representative quotes, and best-fit audiences.
    """
)

st.divider()

st.markdown("### Try a trending search")

suggestions = [
    "杭州三日游",
    "Lululemon leggings",
    "芝加哥咖啡馆",
    "敏感肌面霜",
    "MBA申请"
]

cols = st.columns(len(suggestions))

if "query" not in st.session_state:
    st.session_state["query"] = ""

for i, suggestion in enumerate(suggestions):
    if cols[i].button(suggestion):
        st.session_state["query"] = suggestion

query = st.text_input(
    "Search any topic",
    value=st.session_state["query"],
    placeholder="e.g., 杭州, Aritzia, Chicago brunch, MBA application..."
)

analyze = st.button("Analyze comments", type="primary")

if analyze:
    if not query.strip():
        st.warning("Please enter a topic first.")
    else:
        category = classify_query(query)
        result = generate_insights(query, category)

        positive, neutral, negative = result["sentiment"]

        st.divider()

        st.subheader(f"Analysis for: {query}")
        st.caption(f"Smart category detected: {category}")

        col1, col2, col3 = st.columns(3)
        col1.metric("Positive", f"{positive}%")
        col2.metric("Neutral", f"{neutral}%")
        col3.metric("Negative", f"{negative}%")

        st.progress(positive / 100)

        left, right = st.columns(2)

        with left:
            st.markdown("### ✅ What people like")
            for item in result["likes"]:
                st.write(f"- {item}")

        with right:
            st.markdown("### ⚠️ Common complaints")
            for item in result["complaints"]:
                st.write(f"- {item}")

        st.markdown("### 💬 Representative comments")
        for quote in result["quotes"]:
            st.info(quote)

        st.markdown("### 🎯 Best-fit audience")
        st.success(result["persona"])

        st.markdown("### Product note")
        st.write(
            "This MVP uses a rule-based smart query router to simulate open-ended topic understanding. "
            "In the next version, this layer can be replaced by an LLM API for real-time semantic analysis."
        )

else:
    st.info("Enter a topic or click a trending search to start.")
