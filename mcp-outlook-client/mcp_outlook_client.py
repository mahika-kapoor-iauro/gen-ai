"""
Simplified MCP Outlook Calendar Client
Works with the mcp_outlook_0.1.16 package you have
"""

import asyncio
import json
import os
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("=== MCP Outlook Calendar Client ===\n")
print("Loading configuration...")

# Configuration from .env
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
MCP_SERVER_PATH = os.getenv("MCP_SERVER_PATH", "mcp_outlook_0.1.16/src/mcp_outlook_server/server.py")
DAYS_AHEAD = int(os.getenv("DAYS_AHEAD", "7"))

# Validate configuration
if not SENDER_EMAIL or not SENDER_PASSWORD:
    print("❌ ERROR: Email credentials not found in .env file!")
    print("Please add SENDER_EMAIL and SENDER_PASSWORD to your .env file")
    exit(1)

print(f"✓ Sender email: {SENDER_EMAIL}")
print(f"✓ MCP Server path: {MCP_SERVER_PATH}")
print(f"✓ Looking ahead: {DAYS_AHEAD} days\n")


class SimpleMCPClient:
    """Simplified MCP client for Outlook integration"""
    
    def __init__(self):
        self.user_email = None
        self.calendar_events = []
    
    async def connect_and_fetch(self):
        """Connect to MCP server and fetch data"""
        try:
            # Import MCP client
            from mcp import ClientSession, StdioServerParameters
            from mcp.client.stdio import stdio_client
            
            print("1. Connecting to MCP Outlook server...")
            
            # Set up server parameters
            server_params = StdioServerParameters(
                command="python",
                args=[MCP_SERVER_PATH],
                env=None
            )
            
            # Connect to server
            async with stdio_client(server_params) as (read, write):
                async with ClientSession(read, write) as session:
                    # Initialize session
                    await session.initialize()
                    print("   ✓ Connected to MCP server\n")
                    
                    # List available tools
                    print("2. Discovering available tools...")
                    tools = await session.list_tools()
                    tool_names = [tool.name for tool in tools.tools]
                    print(f"   ✓ Available tools: {', '.join(tool_names)}\n")
                    
                    # Fetch user context
                    print("3. Fetching user information...")
                    await self.get_user_info(session)
                    
                    # Fetch calendar events
                    print("4. Fetching calendar events...")
                    await self.get_calendar_events(session)
                    
            return True
            
        except ImportError as e:
            print(f"❌ Missing package: {e}")
            print("Run: pip install mcp")
            return False
        except Exception as e:
            print(f"❌ Error connecting to MCP server: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    async def get_user_info(self, session):
        """Get user email from MCP server"""
        try:
            # Try different possible tool names
            possible_tools = ["get_user_context", "get_user_info", "get_user"]
            
            for tool_name in possible_tools:
                try:
                    result = await session.call_tool(tool_name, {})
                    user_data = json.loads(result.content[0].text)
                    self.user_email = user_data.get("email") or user_data.get("userPrincipalName")
                    
                    if self.user_email:
                        print(f"   ✓ User email: {self.user_email}\n")
                        return
                except:
                    continue
            
            # If no tool worked, use sender email as fallback
            print("   ⚠ Could not fetch user email from server")
            self.user_email = SENDER_EMAIL
            print(f"   ✓ Using sender email: {self.user_email}\n")
            
        except Exception as e:
            print(f"   ⚠ Warning: {e}")
            self.user_email = SENDER_EMAIL
            print(f"   ✓ Using sender email: {self.user_email}\n")
    
    async def get_calendar_events(self, session):
        """Get calendar events from Outlook"""
        try:
            # Calculate date range
            start_date = datetime.now()
            end_date = start_date + timedelta(days=DAYS_AHEAD)
            
            # Try different possible tool names
            possible_tools = [
                "outlook_get_calendar_events",
                "get_calendar_events",
                "list_calendar_events",
                "get_events"
            ]
            
            for tool_name in possible_tools:
                try:
                    result = await session.call_tool(
                        tool_name,
                        {
                            "start_date": start_date.isoformat(),
                            "end_date": end_date.isoformat()
                        }
                    )
                    
                    events_data = json.loads(result.content[0].text)
                    self.calendar_events = events_data.get("events", events_data.get("value", []))
                    
                    print(f"   ✓ Found {len(self.calendar_events)} upcoming events\n")
                    return
                except:
                    continue
            
            print("   ⚠ No events found or could not fetch events\n")
            
        except Exception as e:
            print(f"   ⚠ Warning: {e}\n")
            self.calendar_events = []
    
    def format_email(self):
        """Format calendar events into HTML email"""
        if not self.calendar_events:
            return """
            <html>
            <body style="font-family: Arial, sans-serif;">
                <h2 style="color: #0078d4;">Your Calendar Summary</h2>
                <p>You have no upcoming events in the next {DAYS_AHEAD} days.</p>
                <p style="color: #666; font-size: 12px;">
                    Generated by MCP Outlook Client
                </p>
            </body>
            </html>
            """.replace("{DAYS_AHEAD}", str(DAYS_AHEAD))
        
        html = """
        <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; padding: 20px; }
                h2 { color: #0078d4; }
                .event {
                    margin: 15px 0;
                    padding: 15px;
                    border-left: 4px solid #0078d4;
                    background-color: #f3f2f1;
                    border-radius: 4px;
                }
                .event-title { 
                    font-weight: bold; 
                    font-size: 16px; 
                    color: #323130;
                    margin-bottom: 8px;
                }
                .event-time { 
                    color: #605e5c; 
                    font-size: 14px;
                    margin-bottom: 5px;
                }
                .event-location {
                    color: #8a8886;
                    font-size: 13px;
                }
                .footer {
                    margin-top: 30px;
                    padding-top: 20px;
                    border-top: 1px solid #edebe9;
                    color: #8a8886;
                    font-size: 12px;
                }
            </style>
        </head>
        <body>
            <h2>📅 Your Upcoming Schedule</h2>
            <p>Here are your events for the next {DAYS_AHEAD} days:</p>
        """.replace("{DAYS_AHEAD}", str(DAYS_AHEAD))
        
        for event in self.calendar_events:
            # Get event details
            subject = event.get('subject', 'No Subject')
            start = event.get('start', {})
            end = event.get('end', {})
            location = event.get('location', {})
            
            # Parse times
            start_dt = datetime.fromisoformat(start.get('dateTime', '').replace('Z', '+00:00'))
            end_dt = datetime.fromisoformat(end.get('dateTime', '').replace('Z', '+00:00'))
            
            # Get location
            location_name = ''
            if isinstance(location, dict):
                location_name = location.get('displayName', '')
            elif isinstance(location, str):
                location_name = location
            
            html += f"""
            <div class="event">
                <div class="event-title">{subject}</div>
                <div class="event-time">
                    📅 {start_dt.strftime('%A, %B %d, %Y')}
                </div>
                <div class="event-time">
                    ⏰ {start_dt.strftime('%I:%M %p')} - {end_dt.strftime('%I:%M %p')}
                </div>
                {f'<div class="event-location">📍 {location_name}</div>' if location_name else ''}
            </div>
            """
        
        html += """
            <div class="footer">
                Generated by MCP Outlook Client<br>
                This is an automated summary of your calendar events.
            </div>
        </body>
        </html>
        """
        
        return html
    
    def send_email(self, html_content):
        """Send email notification"""
        try:
            print("5. Sending email notification...")
            
            # Create message
            message = MIMEMultipart("alternative")
            message["Subject"] = f"Your Schedule Summary - Next {DAYS_AHEAD} Days"
            message["From"] = SENDER_EMAIL
            message["To"] = self.user_email
            
            # Attach HTML content
            html_part = MIMEText(html_content, "html")
            message.attach(html_part)
            
            # Send via Gmail SMTP
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.sendmail(SENDER_EMAIL, self.user_email, message.as_string())
            
            print(f"   ✓ Email sent successfully to {self.user_email}\n")
            return True
            
        except Exception as e:
            print(f"   ❌ Error sending email: {e}")
            print("\n📧 Email content that would have been sent:")
            print("=" * 60)
            print(html_content)
            print("=" * 60)
            return False


async def main():
    """Main execution"""
    print("Starting MCP Outlook Calendar Client...\n")
    
    # Create client
    client = SimpleMCPClient()
    
    # Connect and fetch data
    success = await client.connect_and_fetch()
    
    if not success:
        print("\n❌ Failed to connect to MCP server")
        return
    
    # Format email
    email_content = client.format_email()
    
    # Send email
    client.send_email(email_content)
    
    print("✅ Process completed!")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⚠ Process interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()