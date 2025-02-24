import streamlit as st
import pandas as pd

st.header("Regional Distribution 2024")
st.image("r2024.png", caption="User Activity by Region in 2024")
st.header("Regional Distribution 2025")
st.image("regiondistr.png", caption="User Activity by Region in 2025")
st.write("**Insight:** Maharashtra has surpassed Tennessee in user activity, and new regions like Iowa and Georgia are gaining prominence. This shift suggests evolving engagement patterns across different geographic areas.")

st.header("Country Distribution (2025)")
st.image("c2025.png", caption="User Activity by Country in 2025")
st.write("**Insight:** The platform remains heavily dominated by users from the **United States and India**, with **Poland seeing a significant increase in activity**. Engagement strategies should prioritize these regions to maximize retention.")

st.header("City Distribution (2025)")
st.image("ci2025.png", caption="User Activity by City in 2025")
st.write("**Insight:** **Mumbai and Nashville** remain dominant, with increasing activity in cities like **Spring Hill and Wroclaw**. Targeted engagement strategies in these cities could improve retention and daily usage.")

st.header("User Role Distribution (2024)")
st.image("roledistr2024.png", caption="Role-based Engagement Trends in 2025")
st.header("User Role Distribution (2025)")
st.image("roledistr2025.png", caption="Role-based Engagement Trends in 2025")
st.write("""
**Insight:**  
- **Underwriters dominate the platform.** Ensuring that platform tools are optimized for their workflow can **improve daily retention**.  
- **Admins and Internal users have grown significantly**, suggesting the need for **better management and oversight tools**.  
- **Executives and Leaders are now more engaged.** Adding **high-level insights, reports, and automated dashboards** could further drive engagement.  
- **UA and FS roles have declined**, possibly indicating **disengagement**. Investigating their usage patterns could help **recover lost users**.
""")

st.header("User Engagement: Session Length Analysis")
st.image("sessionlen.png", caption="Guest vs. Registered User Session Length")
st.write("""
📌 **Insight:**  
- **Guest users spend ~44% less time on the platform** than registered users.  
- This suggests **friction in engagement**, possibly due to:
  - **Lack of onboarding**
  - **No incentive to register**
  - **Users passively browsing rather than interacting**
- **Most sessions end after UI rendering,** instead of meaningful actions like **form submissions or button clicks.**  
- **To improve engagement:**  
  - Improve **onboarding for guest users.**  
  - Add **incentives for registration.**  
  - **Encourage deeper interactions** (e.g., personalized recommendations, call-to-action prompts).  
""")

st.header("User Drop-offs: Session Length Distribution")
st.image("dropoffdistr.png", caption="Distribution of Session Lengths")
st.write("""
**Insight:**  
- A large portion of users **drop off within the first 30 seconds of their session**.  
- This suggests that users **aren’t finding value quickly enough** or **are leaving due to UI/UX friction**.  
- **Short session lengths indicate low engagement**, meaning users may be:
  - **Not finding what they need immediately**.
  - **Facing an unintuitive interface**.
  - **Losing interest before interacting with key features**.

**How to Improve Engagement:**  
- Optimize **onboarding experience** to guide users toward valuable actions.  
- Ensure **important content is visible immediately**—reduce friction in navigation.  
- Add **clear calls to action (CTAs)** to encourage further engagement (e.g., "Try Feature X Now!").  
- **Analyze high drop-off pages** to identify problem areas and improve UI/UX.
""")

st.header("Peak User Activity: Events Per Hour")
st.image("perhr.png", caption="User Engagement by Hour")
st.write("""
**Insight:**  
- **Peak engagement occurs around 8 PM**, when most events are recorded.  
- However, **users are primarily browsing (widget:render, view events)** rather than interacting deeply.  
- **Secondary activity peaks** exist in the late afternoon, but engagement drops significantly after 9 PM.

**How to Improve Engagement During Peak Hours:**  
- Implement **calls to action (CTAs) during peak times** to convert passive browsing into meaningful actions.  
- Optimize **platform performance** to handle increased load at **8 PM**.  
- Introduce **real-time engagement features (e.g., notifications, prompts, or personalized recommendations)** to encourage deeper interactions.  
""")

st.header("User Engagement by Day of the Week")
st.image("perweek.png", caption="Platform Activity by Day")
st.write("""
**Insight:**  
- **Tuesday is the peak engagement day**, making it the best time for **feature rollouts, marketing campaigns, and major platform updates**.  
- **Monday to Thursday see consistently high engagement**, indicating strong usage during the workweek.  
- **Weekend activity drops significantly**, especially on **Saturday (lowest engagement day)**, suggesting that users primarily interact with the platform for **work-related tasks**.

**How to Optimize Engagement Based on This Insight:**  
- **Schedule important updates, campaigns, and releases on Tuesdays** to maximize visibility and interaction.  
- **Prioritize workweek engagement strategies**, focusing on Monday-Thursday for key user interactions.  
- **Reconsider weekend-focused efforts**, as engagement is significantly lower, especially on Saturdays.
""")

st.header("Session Duration Patterns: Active vs Passive Engagement")
st.image("avgsessperhr.png", caption="Session Length Trends Throughout the Day")
st.write("""
**Insight:**  
- **Late-night and early-morning session spikes (4 AM, 10-11 PM) suggest passive or automated activity.**  
- **Morning users (6 AM - 10 AM) engage for structured work tasks but don’t stay logged in for extended periods.**  
- **Afternoon sessions (12 PM - 4 PM) are shorter, indicating task-based interactions rather than prolonged engagement.**  
- **Evening sessions (6 PM - 8 PM) show a dip, reinforcing the platform’s work-centric nature.**  
- The **late-night increase** could be due to **either night-owl users or automated non-human activity (batch processes, data retrieval, etc.).**  

**How to Optimize Session Management:**  
- **Investigate whether long late-night sessions are real engagement or passive activity.**  
- **Introduce session timeouts or idle detection** to improve platform efficiency.  
- Optimize platform performance **for actual peak user activity rather than background processes**.  
""")

st.header("Interaction Behavior: Short vs. Long Sessions")
st.image("sessevents.png", caption="Event Distribution in Short vs. Long Sessions")
st.write("""
**Insight:**  
- **Short sessions are dominated by UI rendering & navigation**, with users checking dashboards but not engaging deeply.  
- **Long sessions (3+ hours) also lack strong interaction events**, meaning users are either:
  - **Leaving tabs open without active usage**  
  - **Navigating inefficiently to complete tasks**  
  - **Reviewing data without making edits, updates, or transactions**  
- **Few users engage in meaningful actions (e.g., form submissions, data entry, transactions), regardless of session length.**  

**How to Improve Engagement:**  
- **Introduce engagement nudges** (e.g., “Need help finding something?”).  
- **Optimize workflows** to reduce unnecessary navigation and improve task efficiency.  
- **Detect idle sessions** and prompt users with **actionable next steps (e.g., "Complete your task now")**.  
- **Analyze long-session behaviors** to determine if they are real engagement or passive/automated activity.  
""")

st.header("User Retention & Drop-Off Analysis")
st.image("droppeng.png", caption="Top 10 Users with Largest Drop-Off in Engagement")
st.write("""
**Insight:**  
- Many users **significantly reduced their activity in 2025**, indicating lower retention.  
- Example: **User '61a2808e-1f12-4e32-b1be-7a62225ade2f' had 5,841 events in 2024 but 0 in 2025**, showing complete disengagement.  
- Drop-offs may be related to **workflow inefficiencies, frustration with session experiences, or changing business needs**.

**How to Improve Retention:**  
- **Investigate session performance issues** to reduce potential UX bottlenecks.  
- **Track user frustration signals (e.g., increasing session_end usage)** as early warnings of disengagement.  
- **Engage at-risk users before they drop off**, using proactive outreach, recommendations, or UI nudges.  
- **Improve onboarding & user education**, especially for those switching business units.  
""")

st.header("Stickiness & User Retention Over 28 Days")

# Total Time Spent Per Day
st.header("Total Time Spent Per Day (Days 11 to 28)")
st.image("timeperday.png", caption="Total Time Spent Per Day (Days 11-28)")
st.write("""
**Insight:**  
- Time spent is generally **low and stable** until **a massive spike around Day 26**.  
- Smaller fluctuations around **Days 14-16** suggest periodic bursts of engagement.  
- The **spike at Day 26** is likely an **outlier or an external trigger (e.g., event, update, or bot activity).**  

**Possible Causes:**  
- Users **spend limited time daily** but occasionally **engage deeply** on certain days.  
- The **Day 26 spike may be due to abnormal session durations, automated scripts, or a one-time event.**  

**Next Steps to Improve Engagement:**  
- Investigate **why engagement spiked at Day 26** (real user activity vs. technical artifact).  
- Encourage **consistent engagement patterns** rather than one-time deep usage.  
- Use **interactive features** (recommendations, tasks, notifications) to sustain user interaction.
""")
# Return User Analysis
st.header("Return User Analysis")
st.image("returnuseranal.png", caption="Return User Analysis: Returning vs. Non-Returning Users")
st.write("""
**Insight:**  
- A **large portion of users return** (orange bars), but there is also a significant number of **one-time users (blue bars).**  
- A **few users return at extremely high frequencies**, while most return occasionally.  
- **Wide variation in return rates** suggests different user segments:  
  - **Highly engaged users** (frequent returns).  
  - **Casual users** (occasional returns).  
  - **One-time visitors** (do not return).  

**Possible Causes:**  
- Some users may be **exploring the platform briefly before dropping off.**  
- Frequent returners may be **power users, admins, or users with complex workflows.**  
- Non-returners may have **faced usability issues or not found enough value.**  

**Next Steps to Improve Retention:**  
- Identify **top returners** and analyze their behaviors to **replicate their engagement patterns**.  
- Investigate why **one-time users drop off** (feedback surveys, exit interviews).  
- Offer **personalized re-engagement strategies** (reminders, tutorials, targeted content) to casual users.  
""")


# User Return Rate Over 28 Days
st.header("User Return Rate Over 28 Days")
st.image("usrreturn28.png", caption="User Return Rate Over 28 Days")
st.write("""
**Insight:**  
- **Return rate remains high early on (~95-100%) but drops significantly around Day 20.**  
- A **steep decline between Days 20-23** suggests many users disengage at this point.  
- The **spike at the end** suggests a possible **data anomaly** or a sudden event that brought users back.  

**Possible Causes:**  
- Users may **complete their primary tasks within the first 20 days**, leading to lower return rates after.  
- **Lack of engagement triggers (e.g., reminders, follow-ups)** may cause users to drop off.  
- A **sudden return spike** could indicate **a campaign, update, or forced login event.**  

**Next Steps to Improve Stickiness:**  
- Implement **re-engagement strategies** around **Days 15-20** (emails, notifications, reminders).  
- Analyze what **caused the return spike at the end** to replicate that effect.  
- Encourage **long-term usage patterns** by introducing **continuous engagement features**.
""")

