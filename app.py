import streamlit as st
from commands import RedisCommands
from Persistence import Persistence
from config import PERSISTENCE_FILE

# Initialize database and persistence
db_commands = RedisCommands()
persistence = Persistence(db_commands.db, PERSISTENCE_FILE)
persistence.load_data()

st.title('Redis-Like Database Interface')

# Define layout for commands
with st.sidebar:
    st.header('Commands')
    command = st.selectbox('Select Command', ['SET', 'GET', 'DEL', 'EXPIRE', 'KEYS', 'PERSIST'])
    key = st.text_input('Key', '')
    value = st.text_input('Value', '')
    ttl = st.number_input('TTL (seconds)', min_value=0, value=0)
    if st.button('Execute'):
        if command == 'SET' and key and value:
            result = db_commands.handle_command(command, key, value)
        elif command == 'GET' and key:
            result = db_commands.handle_command(command, key)
        elif command == 'DEL' and key:
            result = db_commands.handle_command(command, key)
        elif command == 'EXPIRE' and key and ttl:
            result = db_commands.handle_command(command, key, ttl)
        elif command == 'KEYS':
            result = db_commands.handle_command(command)
        elif command == 'PERSIST' and key:
            result = db_commands.handle_command(command, key)
        else:
            result = "Invalid command or missing parameters."

        st.write(f'Result: {result}')

# Display current data
st.subheader('Current Data')
data = db_commands.db.store
if not data:
    st.write('No data available.')
else:
    for k, v in data.items():
        st.write(f'Key: {k}, Value: {v}')
