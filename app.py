import streamlit as st

st.set_page_config(page_title="CommentLens", page_icon="🔍", layout="wide")


def classify_query(query):
    q = query.lower()
    if any(k in q for k in ["咖啡", "coffee", "cafe", "餐厅", "restaurant", "brunch", "甜品", "dessert"]):
        return "Food & Places"
    if any(k in q for k in ["杭州", "上海", "北京", "东京", "旅行", "旅游", "trip", "travel", "hotel"]):
        return "Travel"
    if any(k in q for k in ["面霜", "护肤", "口红", "防晒", "敏感肌", "skincare", "makeup", "beauty"]):
        return "Beauty"
    if any(k in q for k in ["lululemon", "aritzia", "穿搭", "衣服", "包", "fashion", "outfit"]):
        return "Fashion"
    if any(k in q for k in ["mba", "留学", "申请", "大学", "graduate", "school"]):
        return "Education"
    if any(k in q for k in ["ai", "chatgpt", "app", "软件", "产品", "tech"]):
        return "Tech"
    return "Lifestyle"


def get_recommendations(query):
    q = query.lower()

    if ("芝加哥" in q or "chicago" in q) and any(k in q for k in ["咖啡", "coffee", "cafe"]):
        return {
            "title": "芝加哥咖啡馆推荐",
            "summary": "检测到这是地点推荐类搜索。CommentLens 会优先输出具体店铺，而不是泛泛总结“咖啡馆”这个品类。",
            "items": [
                {
                    "name": "Sawada Coffee",
                    "score": 88,
                    "sentiment": "Positive",
                    "why": "抹茶拿铁、工业风空间和拍照氛围被频繁提到。",
                    "best_for": "第一次来芝加哥、朋友聊天、拍照打卡",
                    "watch_out": "周末可能排队，座位不稳定。",
                    "pattern": "正面评论集中在饮品记忆点和空间氛围；负面评论主要是拥挤和等待时间。",
                    "quotes": [
                        "“The matcha latte is the reason I would come back.”",
                        "“Great vibe, but I would avoid weekend rush hour.”"
                    ]
                },
                {
                    "name": "The Wormhole Coffee",
                    "score": 84,
                    "sentiment": "Positive",
                    "why": "复古主题、Wicker Park 社区感和独特空间风格很受欢迎。",
                    "best_for": "独自学习、复古爱好者、周末放松",
                    "watch_out": "空间偏小，不适合大组聚会。",
                    "pattern": "评论常说它比普通连锁咖啡馆更有记忆点，但座位和空间是限制。",
                    "quotes": [
                        "“The vibe is more special than a regular coffee shop.”",
                        "“Cute place, but seats fill up quickly.”"
                    ]
                },
                {
                    "name": "Intelligentsia Coffee",
                    "score": 81,
                    "sentiment": "Positive",
                    "why": "咖啡品质稳定，适合真正关注咖啡豆和口味的人。",
                    "best_for": "咖啡爱好者、工作间隙、低风险选择",
                    "watch_out": "氛围感不如独立小店强。",
                    "pattern": "正面评论强调咖啡本身质量；较弱评论认为体验偏功能性。",
                    "quotes": [
                        "“The coffee itself is strong and reliable.”",
                        "“Good for coffee, not necessarily for a long hangout.”"
                    ]
                },
                {
                    "name": "La Colombe",
                    "score": 78,
                    "sentiment": "Stable",
                    "why": "稳定、方便、出错率低，适合快速买咖啡。",
                    "best_for": "通勤、学习、快速补咖啡因",
                    "watch_out": "缺少独特体验感。",
                    "pattern": "评论稳定但情绪不强，用户更看重可靠性而不是惊喜感。",
                    "quotes": [
                        "“Reliable coffee when I do not want to take risks.”",
                        "“Good quality, but not the most memorable cafe.”"
                    ]
                }
            ]
        }

    if "杭州" in q and any(k in q for k in ["咖啡", "餐厅", "美食", "cafe", "food", "brunch"]):
        return {
            "title": "杭州咖啡馆 / 美食推荐",
            "summary": "检测到这是城市 + 消费决策类搜索。CommentLens 会输出具体推荐类型和评论信号。",
            "items": [
                {
                    "name": "西湖周边景观咖啡馆",
                    "score": 86,
                    "sentiment": "Positive",
                    "why": "风景、散步路线和拍照体验被频繁提到。",
                    "best_for": "游客、情侣、周末慢旅行",
                    "watch_out": "节假日人流大，部分店价格偏高。",
                    "pattern": "正面评论集中在景观和氛围；负面评论集中在拥挤和性价比。",
                    "quotes": [
                        "“The view is beautiful, but avoid national holidays.”",
                        "“Good for photos and slow walks.”"
                    ]
                },
                {
                    "name": "武林 / 嘉里中心周边餐厅",
                    "score": 80,
                    "sentiment": "Stable",
                    "why": "位置方便、选择多，适合不想做太多攻略的人。",
                    "best_for": "第一次来杭州、朋友聚餐、多人出行",
                    "watch_out": "本地特色不一定强。",
                    "pattern": "评论强调便利性，而不是惊喜感。",
                    "quotes": [
                        "“Easy choice when you do not want to plan too much.”",
                        "“Convenient, but not the most local experience.”"
                    ]
                },
                {
                    "name": "本地面馆和小吃店",
                    "score": 83,
                    "sentiment": "Positive",
                    "why": "更有本地感，性价比通常比景区餐厅更好。",
                    "best_for": "美食探索、预算有限、本地体验",
                    "watch_out": "环境可能普通，不一定适合拍照。",
                    "pattern": "正面评论集中在味道和价格；负面评论主要是环境简单。",
                    "quotes": [
                        "“Small local places are more worth it than tourist restaurants.”",
                        "“Not fancy, but the taste feels more authentic.”"
                    ]
                }
            ]
        }

    return None


def generate_insights(query, category):
    templates = {
        "Food & Places": {
            "sentiment": (69, 20, 11),
            "confidence": 76,
            "summary": f"{query} 的评论整体偏正面，但用户真正关心的是 taste, atmosphere, price-value, waiting time 和是否值得专门去。",
            "confidence_reason": "中高可信度：餐饮类评论通常会明确提到味道、价格、环境、排队和地理位置。但当前 MVP 没有接入实时 API，因此是基于模拟评论模式。",
            "likes": ["氛围和拍照价值容易带来正面评价。", "朋友聚会、约会、探店场景会提高推荐意愿。", "具体菜品或饮品被反复提及时，可信度更高。"],
            "complaints": ["排队和拥挤是常见负面点。", "部分用户会质疑性价比。", "不同门店、时间段体验差异较大。"],
            "themes": ["Taste", "Atmosphere", "Price-value", "Waiting time", "Photo appeal"],
            "decision": "如果你重视氛围和社交体验，值得尝试；如果你只看性价比，需要重点看负面评论。",
            "risks": ["泛搜索会混合很多不同需求。", "网红店可能被视觉内容放大。", "评论可能受访问时间影响。"],
            "recommendations": ["进一步搜索“适合学习 / 适合约会 / 值不值得排队”。", "优先看近期评论。", "同时比较好评和差评。"],
            "quotes": [f"“{query} looks good, but I would check whether it is worth the wait.”", "“The vibe matters as much as the food itself.”", "“Good for photos, but price-value depends on what you order.”"],
            "persona": "适合 foodies、朋友聚会、喜欢氛围感和社交分享的人。"
        },
        "Travel": {
            "sentiment": (72, 18, 10),
            "confidence": 82,
            "summary": f"{query} 的评论通常偏正面，但决策重点在景色、路线、交通、人流和是否适合自己的旅行方式。",
            "confidence_reason": "高可信度：旅行评论通常围绕清晰维度展开，例如景点、交通、拥挤程度、住宿和预算。",
            "likes": ["景色和拍照体验经常被称赞。", "本地美食和咖啡馆会提高整体体验。", "适合周末短途旅行的讨论很多。"],
            "complaints": ["节假日人流是最大问题。", "交通和路线规划可能比较累。", "热门景点可能商业化。"],
            "themes": ["Scenery", "Crowds", "Transportation", "Food", "Planning"],
            "decision": "如果避开高峰期并提前规划路线，整体值得考虑。",
            "risks": ["旅行评论季节性很强。", "网红照片可能美化真实体验。", "不同旅行风格评价差异很大。"],
            "recommendations": ["按一日游、周末游、情侣游等场景细化搜索。", "重点看交通和拥挤相关差评。", "找和自己旅行风格相似的评论。"],
            "quotes": [f"“{query} is beautiful, but avoid peak season.”", "“Planning ahead makes the experience much better.”", "“Hidden local spots are more interesting than famous ones.”"],
            "persona": "适合周末旅行者、情侣、美食爱好者和喜欢拍照的人。"
        },
        "Lifestyle": {
            "sentiment": (58, 29, 13),
            "confidence": 65,
            "summary": f"{query} 的讨论比较分散，适合做趋势探索，但需要进一步细化问题才能得到强推荐。",
            "confidence_reason": "中低可信度：宽泛生活方式搜索通常混合多种意图，信号不够集中。",
            "likes": ["用户好奇心强。", "个人经验类评论多。", "适合发现趋势和痛点。"],
            "complaints": ["评论主观性强。", "不同人需求差异大。", "泛搜索不容易得到明确结论。"],
            "themes": ["Preference", "Trend", "Emotion", "Use case"],
            "decision": "适合初步探索，但不适合直接做决策。",
            "risks": ["搜索意图太宽。", "用户群体混杂。", "爆款内容可能影响判断。"],
            "recommendations": ["加入城市、预算、使用场景等限制。", "对比不同评论群体。", "优先用负面评论识别风险。"],
            "quotes": [f"“{query} has mixed reviews, so I checked multiple posts.”", "“The comments are more useful than the post itself.”", "“It depends a lot on personal preference.”"],
            "persona": "适合趋势探索者和轻量研究用户。"
        }
    }
    return templates.get(category, templates["Lifestyle"])


def display_recommendations(data):
    st.subheader(data["title"])
    st.write(data["summary"])
    st.markdown("### Ranked recommendations")

    for i, item in enumerate(data["items"], 1):
        with st.container(border=True):
            c1, c2, c3 = st.columns([2.3, 1, 1])
            with c1:
                st.markdown(f"### {i}. {item['name']}")
                st.write(f"**推荐理由：** {item['why']}")
                st.write(f"**适合：** {item['best_for']}")
                st.write(f"**注意：** {item['watch_out']}")
            with c2:
                st.metric("Confidence", f"{item['score']}/100")
            with c3:
                st.metric("Sentiment", item["sentiment"])

            st.write(f"**评论模式：** {item['pattern']}")
            st.markdown("**代表评论**")
            for quote in item["quotes"]:
                st.info(quote)


def display_insights(query, category, result):
    p, n, neg = result["sentiment"]

    st.subheader(f"Insight report: {query}")
    st.caption(f"Smart category detected: {category}")

    st.markdown("### Quick summary")
    st.write(result["summary"])

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Positive", f"{p}%")
    c2.metric("Neutral", f"{n}%")
    c3.metric("Negative", f"{neg}%")
    c4.metric("Confidence", f"{result['confidence']}/100")

    st.progress(p / 100)

    st.markdown("### Comment Confidence Analysis")
    st.write(result["confidence_reason"])

    left, right = st.columns(2)
    with left:
        st.markdown("### What people like")
        for x in result["likes"]:
            st.write(f"✅ {x}")
    with right:
        st.markdown("### Common complaints")
        for x in result["complaints"]:
            st.write(f"⚠️ {x}")

    st.markdown("### Key comment themes")
    st.write(" · ".join(result["themes"]))

    st.markdown("### Decision signal")
    st.success(result["decision"])

    a, b = st.columns(2)
    with a:
        st.markdown("### Risk signals")
        for x in result["risks"]:
            st.write(f"🚩 {x}")
    with b:
        st.markdown("### Actionable recommendations")
        for x in result["recommendations"]:
            st.write(f"💡 {x}")

    st.markdown("### Representative comments")
    for quote in result["quotes"]:
        st.info(quote)

    st.markdown("### Best-fit audience")
    st.success(result["persona"])


st.title("🔍 CommentLens")
st.caption("Turn social comments into decision-ready consumer insights.")

st.markdown("""
CommentLens supports two MVP modes:

**Recommendation Mode** — for searches like “芝加哥咖啡馆” or “杭州咖啡馆,” returning specific ranked places.  
**Insight Mode** — for broader product, brand, travel, school, and lifestyle topics.
""")

st.divider()

suggestions = ["芝加哥咖啡馆", "杭州咖啡馆", "Lululemon leggings", "敏感肌面霜", "MBA申请"]

if "query" not in st.session_state:
    st.session_state["query"] = ""

cols = st.columns(len(suggestions))
for i, s in enumerate(suggestions):
    if cols[i].button(s):
        st.session_state["query"] = s

query = st.text_input(
    "Search any topic",
    value=st.session_state["query"],
    placeholder="e.g., 芝加哥咖啡馆, 杭州餐厅, Aritzia, MBA申请..."
)

if st.button("Analyze comments", type="primary"):
    if not query.strip():
        st.warning("Please enter a topic first.")
    else:
        st.divider()
        rec_data = get_recommendations(query)

        if rec_data:
            st.caption("Detected mode: Recommendation Mode")
            display_recommendations(rec_data)
        else:
            category = classify_query(query)
            st.caption("Detected mode: Insight Mode")
            result = generate_insights(query, category)
            display_insights(query, category, result)

        st.divider()
        st.markdown("### MVP note")
        st.write(
            "This demo uses a rule-based smart query router and curated mock comment patterns to simulate the product experience without paid APIs. "
            "The next version can replace this layer with a live LLM/search API and real social-comment data."
        )
else:
    st.info("Enter a topic or click a trending search to start.")
