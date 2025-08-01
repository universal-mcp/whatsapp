
from universal_mcp.servers import SingleMCPServer
from universal_mcp.integrations import AgentRIntegration
from universal_mcp.stores import EnvironmentStore
from universal_mcp.exceptions import NotAuthorizedError
from universal_mcp.utils.agentr import AgentrClient
import httpx

from universal_mcp_whatsapp.app import WhatsappApp

env_store = EnvironmentStore()
integration_instance = AgentRIntegration(name="whatsapp", store=env_store,  client=AgentrClient(api_key="sk_416e4f88-3beb-4a79-a0ef-fb1d2c095aee",base_url="https://api.agentr.dev"))

try:
    integration_instance.get_credentials()
    app_instance = WhatsappApp(integration=integration_instance)
    print("✅ Using AgentR integration for WhatsApp")
except (NotAuthorizedError, httpx.HTTPStatusError):
    app_instance = WhatsappApp(integration=None)
    print("⚠️ No AgentR integration found, using direct WhatsApp authentication")

mcp = SingleMCPServer(
    app_instance=app_instance,
)

if __name__ == "__main__":
    mcp.run(transport="sse")


