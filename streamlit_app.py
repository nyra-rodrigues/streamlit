import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast

# Load your dataset (ensure it's preloaded in your session, or load it dynamically)
# Example: 
combined_df_2025 = pd.read_csv('amplitude_export_chunk_1_anonymized_subchunk_200000_300000.csv')
df = pd.read_csv('amplitude_export_chunk_1_anonymized_subchunk_200000_300000.csv')

# Streamlit Dashboard Title
st.title('User Behavior and Session Analysis Dashboard')

# Section 1: Role Distribution
st.header("1. Role Distribution")
combined_df_2025['user_properties'] = combined_df_2025['user_properties'].apply(lambda x: ast.literal_eval(x))
combined_df_2025['roles'] = combined_df_2025['user_properties'].apply(lambda x: x.get('roles', []))
roles = combined_df_2025['roles'].explode().value_counts()

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=roles.index, y=roles.values, ax=ax)
ax.set_title("Role Distribution")
ax.set_xlabel("Role")
ax.set_ylabel("Count")
plt.xticks(rotation=90)
st.pyplot(fig)

# Section 2: Session Length Analysis
st.header("2. Session Length Analysis")
df['server_received_time'] = pd.to_datetime(df['server_received_time'], errors='coerce')
df_sessions = df.groupby('session_id')['server_received_time'].agg(['min', 'max'])
df_sessions['session_length'] = (df_sessions['max'] - df_sessions['min']).dt.total_seconds()
df = df.merge(df_sessions[['session_length']], left_on='session_id', right_index=True)

st.subheader("Average Session Length")
avg_registered = df[df['user_id'] != 'EMPTY']['session_length'].mean()
avg_guest = df[df['user_id'] == 'EMPTY']['session_length'].mean()

st.write(f"Average session length (registered users): {avg_registered:.2f} seconds")
st.write(f"Average session length (guest users): {avg_guest:.2f} seconds")

# Plot session length distribution
fig, ax = plt.subplots(figsize=(10, 6))
df_sessions.groupby(df_sessions.index)['session_length'].mean().sort_values(ascending=True).head(10).plot(kind='bar', ax=ax)
ax.set_title("Top 10 Session Lengths")
ax.set_xlabel("Session ID")
ax.set_ylabel("Session Length (Seconds)")
st.pyplot(fig)

# Section 3: Time Difference Between Event and Upload
st.header("3. Time Difference Between Event and Upload")

# Calculate time difference
combined_df_2025['client_event_time'] = pd.to_datetime(combined_df_2025['client_event_time'])
combined_df_2025['client_upload_time'] = pd.to_datetime(combined_df_2025['client_upload_time'])
combined_df_2025['time_difference'] = combined_df_2025['client_upload_time'] - combined_df_2025['client_event_time']
combined_df_2025['time_difference_minutes'] = combined_df_2025['time_difference'].dt.total_seconds() / 60

st.subheader("Time Difference Summary")
st.write(combined_df_2025['time_difference_minutes'].describe())

# Filter and visualize upload times > 10 days
filtered_df_2025 = combined_df_2025[combined_df_2025['time_difference_minutes'] > 14400]
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(x='country', data=filtered_df_2025, ax=ax)
ax.set_xlabel('Countries with Upload Time > 10 Days')
ax.set_ylabel('Frequency')
ax.set_title('Country Distribution of Upload Time > 10 Days')
plt.xticks(rotation=45)
st.pyplot(fig)

# Section 4: User Drop-offs Between 2024 and 2025
st.header("4. User Drop-offs Between 2024 and 2025")

# Filter users with drop-offs
filtered_users = row_count_df[(row_count_df['2025'] + 50) <= row_count_df['2024']]
dropoff_users_df_2024 = filtered_df_2024[filtered_df_2024['user_id'].isin(filtered_users['user_id'])]
dropoff_users_df_2025 = combined_df_2025[combined_df_2025['user_id'].isin(filtered_users['user_id'])]

# Plot drop-off analysis
st.subheader("User Drop-off Analysis")
st.write(f"Number of drop-off users between 2024 and 2025: {len(filtered_users)}")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(dropoff_users_df_2024['client_event_time'], kde=True, label='2024', color='blue', ax=ax)
sns.histplot(dropoff_users_df_2025['client_event_time'], kde=True, label='2025', color='red', ax=ax)
ax.set_title('Event Time Distribution for Drop-off Users (2024 vs. 2025)')
ax.set_xlabel('Event Time')
ax.set_ylabel('Frequency')
plt.legend()
st.pyplot(fig)

# Section 5: Return Rate Analysis
st.header("5. Return Rate Analysis Over 28 Days")

# Calculate return rate
first_period_2024['timestamp'] = pd.to_datetime(first_period_2024['client_event_time'])
first_period_2024 = first_period_2024.sort_values(by=['user_id', 'client_event_time'])
first_period_2024['time_diff'] = first_period_2024.groupby('user_id')['client_event_time'].diff()
return_threshold = pd.Timedelta(days=1)
first_period_2024['is_return'] = first_period_2024['time_diff'].apply(lambda x: x <= return_threshold if pd.notnull(x) else False)

# Plot return rate
st.subheader("Return Rate Over Time")
cohort_analysis = first_period_2024.groupby('timestamp')['is_return'].mean().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=cohort_analysis, x='timestamp', y='is_return', ax=ax, marker='o')
ax.set_title('User Return Rate Over 28 Days')
ax.set_xlabel('Day')
ax.set_ylabel('Return Rate')
plt.grid(True)
st.pyplot(fig)

# Add interactive widgets for user input (optional)
st.sidebar.header('Filters')
selected_role = st.sidebar.selectbox('Select Role', roles.index)
filtered_by_role = combined_df_2025[combined_df_2025['roles'].apply(lambda x: selected_role in x)]

st.write(f"Showing data for role: {selected_role}")
st.write(filtered_by_role)

