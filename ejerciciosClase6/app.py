import streamlit as st
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

st.set_page_config(
    page_title="Cliente MCP",
    page_icon="🔧",
    layout="wide"
)

class MCPClient:
    def __init__(self):
        self.session = None
        self.available_tools = []

    async def connect(self, server_script_path: str):
        server_params = StdioServerParameters(
            command="python",
            args=[server_script_path],
        )
        self.stdio_transport = await stdio_client(server_params)
        read_stream, write_stream = self.stdio_transport
        self.session = await ClientSession(read_stream, write_stream)
        await self.session.initialize()
        response = await self.session.list_tools()
        self.available_tools = response.tools

    async def call_tool(self, tool_name: str, tool_args: dict):
        return await self.session.call_tool(tool_name, tool_args)

st.title("Cliente MCP con Streamlit")
st.sidebar.header("Configuración")
server_path = st.sidebar.text_input("Ruta al servidor MCP", value="server.py")
connect_button = st.sidebar.button("Conectar al servidor")

if "client" not in st.session_state:
    st.session_state.client = MCPClient()
if "connected" not in st.session_state:
    st.session_state.connected = False

if connect_button:
    asyncio.run(st.session_state.client.connect(server_path))
    st.session_state.connected = True

if st.session_state.connected:
    st.sidebar.success("Conectado al servidor MCP")
    st.sidebar.subheader("Herramientas disponibles")
    for tool in st.session_state.client.available_tools:
        st.sidebar.write(f"🔧 {tool.name}: {tool.description}")

user_input = st.text_input("Escribe tu mensaje:")
if user_input and st.session_state.connected:
    st.write(f"Procesando: {user_input}")