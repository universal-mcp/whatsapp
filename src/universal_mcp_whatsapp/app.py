from typing import List, Dict, Any, Optional
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration
from universal_mcp_whatsapp.whatsapp import (
    search_contacts as whatsapp_search_contacts,
    list_messages as whatsapp_list_messages,
    list_chats as whatsapp_list_chats,
    get_chat as whatsapp_get_chat,
    get_direct_chat_by_contact as whatsapp_get_direct_chat_by_contact,
    get_contact_chats as whatsapp_get_contact_chats,
    get_last_interaction as whatsapp_get_last_interaction,
    get_message_context as whatsapp_get_message_context,
    send_message as whatsapp_send_message,
    send_file as whatsapp_send_file,
    send_audio_message as whatsapp_audio_voice_message,
    download_media as whatsapp_download_media,
)

class WhatsappApp(APIApplication):
    """
    Base class for Universal MCP Applications.
    """
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="whatsapp", integration=integration, **kwargs)

    

    def search_contacts(
        self,
        query: str,
        user_id: str = "default_user",
    ) -> List[Dict[str, Any]]:
        """
        Search WhatsApp contacts by name or phone number.

        Args:
            query (string): Search term to match against contact names or phone numbers
            user_id (string): The user ID to search contacts for (default: "default_user")

        Returns:
            List[Dict[str, Any]]: Retrieved collection

        Raises:
            ValueError: Raised when required parameters are missing.

        Tags:
            whatsapp.contacts, important
        """
        if query is None:
            raise ValueError("Missing required parameter 'query'.")
        contacts = whatsapp_search_contacts(query, user_id)
        return contacts

    def list_messages(
        self,
        after: Optional[str] = None,
        before: Optional[str] = None,
        sender_phone_number: Optional[str] = None,
        chat_jid: Optional[str] = None,
        query: Optional[str] = None,
        limit: int = 20,
        page: int = 0,
        include_context: bool = True,
        context_before: int = 1,
        context_after: int = 1,
        user_id: str = "default_user",
    ) -> List[Dict[str, Any]]:
        """
        Get WhatsApp messages matching specified criteria with optional context.

        Args:
            after (string): Optional ISO-8601 formatted string to only return messages after this date
            before (string): Optional ISO-8601 formatted string to only return messages before this date
            sender_phone_number (string): Optional phone number to filter messages by sender
            chat_jid (string): Optional chat JID to filter messages by chat
            query (string): Optional search term to filter messages by content
            limit (integer): Maximum number of messages to return (default 20)
            page (integer): Page number for pagination (default 0)
            include_context (boolean): Whether to include messages before and after matches (default True)
            context_before (integer): Number of messages to include before each match (default 1)
            context_after (integer): Number of messages to include after each match (default 1)
            user_id (string): The user ID to get messages for (default: "default_user")

        Returns:
            List[Dict[str, Any]]: Retrieved collection

        Raises:
            ValueError: Raised when required parameters are missing.

        Tags:
            whatsapp.messages, important
        """
        messages = whatsapp_list_messages(
            after=after,
            before=before,
            sender_phone_number=sender_phone_number,
            chat_jid=chat_jid,
            query=query,
            limit=limit,
            page=page,
            include_context=include_context,
            context_before=context_before,
            context_after=context_after,
            user_id=user_id,
        )
        return messages

    def list_chats(
        self,
        query: Optional[str] = None,
        limit: int = 20,
        page: int = 0,
        include_last_message: bool = True,
        sort_by: str = "last_active",
        user_id: str = "default_user",
    ) -> List[Dict[str, Any]]:
        """
        Get WhatsApp chats matching specified criteria.

        Args:
            query (string): Optional search term to filter chats by name or JID
            limit (integer): Maximum number of chats to return (default 20)
            page (integer): Page number for pagination (default 0)
            include_last_message (boolean): Whether to include the last message in each chat (default True)
            sort_by (string): Field to sort results by, either "last_active" or "name" (default "last_active")
            user_id (string): The user ID to get chats for (default: "default_user")

        Returns:
            List[Dict[str, Any]]: Retrieved collection

        Raises:
            ValueError: Raised when required parameters are missing.

        Tags:
            whatsapp.chats, important
        """
        chats = whatsapp_list_chats(
            query=query,
            limit=limit,
            page=page,
            include_last_message=include_last_message,
            sort_by=sort_by,
            user_id=user_id,
        )
        return chats

    def get_chat(
        self,
        chat_jid: str,
        include_last_message: bool = True,
        user_id: str = "default_user",
    ) -> Dict[str, Any]:
        """
        Get WhatsApp chat metadata by JID.

        Args:
            chat_jid (string): The JID of the chat to retrieve
            include_last_message (boolean): Whether to include the last message (default True)
            user_id (string): The user ID to get chat for (default: "default_user")

        Returns:
            Dict[str, Any]: Retrieved chat metadata

        Raises:
            ValueError: Raised when required parameters are missing.

        Tags:
            whatsapp.chat, important
        """
        if chat_jid is None:
            raise ValueError("Missing required parameter 'chat_jid'.")
        chat = whatsapp_get_chat(chat_jid, include_last_message, user_id)
        return chat

    def get_direct_chat_by_contact(
        self,
        sender_phone_number: str,
        user_id: str = "default_user",
    ) -> Dict[str, Any]:
        """
        Get WhatsApp chat metadata by sender phone number.

        Args:
            sender_phone_number (string): The phone number to search for
            user_id (string): The user ID to get chat for (default: "default_user")

        Returns:
            Dict[str, Any]: Retrieved chat metadata

        Raises:
            ValueError: Raised when required parameters are missing.

        Tags:
            whatsapp.chat, important
        """
        if sender_phone_number is None:
            raise ValueError("Missing required parameter 'sender_phone_number'.")
        chat = whatsapp_get_direct_chat_by_contact(sender_phone_number, user_id)
        return chat

    def get_contact_chats(
        self,
        jid: str,
        limit: int = 20,
        page: int = 0,
        user_id: str = "default_user",
    ) -> List[Dict[str, Any]]:
        """
        Get all WhatsApp chats involving the contact.

        Args:
            jid (string): The contact's JID to search for
            limit (integer): Maximum number of chats to return (default 20)
            page (integer): Page number for pagination (default 0)
            user_id (string): The user ID to get chats for (default: "default_user")

        Returns:
            List[Dict[str, Any]]: Retrieved collection

        Raises:
            ValueError: Raised when required parameters are missing.

        Tags:
            whatsapp.contact_chats, important
        """
        if jid is None:
            raise ValueError("Missing required parameter 'jid'.")
        chats = whatsapp_get_contact_chats(jid, limit, page, user_id)
        return chats

    def get_last_interaction(
        self,
        jid: str,
        user_id: str = "default_user",
    ) -> str:
        """
        Get most recent WhatsApp message involving the contact.

        Args:
            jid (string): The JID of the contact to search for
            user_id (string): The user ID to get interaction for (default: "default_user")

        Returns:
            string: Retrieved message

        Raises:
            ValueError: Raised when required parameters are missing.

        Tags:
            whatsapp.interaction, important
        """
        if jid is None:
            raise ValueError("Missing required parameter 'jid'.")
        message = whatsapp_get_last_interaction(jid, user_id)
        return message

    def get_message_context(
        self,
        message_id: str,
        before: int = 5,
        after: int = 5,
        user_id: str = "default_user",
    ) -> Dict[str, Any]:
        """
        Get context around a specific WhatsApp message.

        Args:
            message_id (string): The ID of the message to get context for
            before (integer): Number of messages to include before the target message (default 5)
            after (integer): Number of messages to include after the target message (default 5)
            user_id (string): The user ID to get context for (default: "default_user")

        Returns:
            Dict[str, Any]: Retrieved message context

        Raises:
            ValueError: Raised when required parameters are missing.

        Tags:
            whatsapp.message_context, important
        """
        if message_id is None:
            raise ValueError("Missing required parameter 'message_id'.")
        context = whatsapp_get_message_context(message_id, before, after, user_id)
        return context

    def send_message(
        self,
        recipient: str,
        message: str,
        user_id: str = "default_user",
    ) -> Dict[str, Any]:
        """
        Send a WhatsApp message to a person or group. For group chats use the JID.

        Args:
            recipient (string): The recipient - either a phone number with country code but no + or other symbols,
                             or a JID (e.g., "123456789@s.whatsapp.net" or a group JID like "123456789@g.us")
            message (string): The message text to send
            user_id (string): The user ID to send message from (default: "default_user")

        Returns:
            Dict[str, Any]: A dictionary containing success status and a status message

        Raises:
            ValueError: Raised when required parameters are missing.

        Tags:
            whatsapp.send_message, important
        """
        if recipient is None:
            raise ValueError("Missing required parameter 'recipient'.")
        if message is None:
            raise ValueError("Missing required parameter 'message'.")
        
        # Call the whatsapp_send_message function with the unified recipient parameter
        success, status_message = whatsapp_send_message(recipient, message, user_id)
        return {
            "success": success,
            "message": status_message,
        }

    def send_file(
        self,
        recipient: str,
        media_path: str,
        user_id: str = "default_user",
    ) -> Dict[str, Any]:
        """
        Send a file such as a picture, raw audio, video or document via WhatsApp to the specified recipient. For group messages use the JID.

        Args:
            recipient (string): The recipient - either a phone number with country code but no + or other symbols,
                             or a JID (e.g., "123456789@s.whatsapp.net" or a group JID like "123456789@g.us")
            media_path (string): The absolute path to the media file to send (image, video, document)
            user_id (string): The user ID to send file from (default: "default_user")

        Returns:
            Dict[str, Any]: A dictionary containing success status and a status message

        Raises:
            ValueError: Raised when required parameters are missing.

        Tags:
            whatsapp.send_file, important
        """
        if recipient is None:
            raise ValueError("Missing required parameter 'recipient'.")
        if media_path is None:
            raise ValueError("Missing required parameter 'media_path'.")
        
        # Call the whatsapp_send_file function
        success, status_message = whatsapp_send_file(recipient, media_path, user_id)
        return {
            "success": success,
            "message": status_message,
        }

    def send_audio_message(
        self,
        recipient: str,
        media_path: str,
        user_id: str = "default_user",
    ) -> Dict[str, Any]:
        """
        Send any audio file as a WhatsApp audio message to the specified recipient. For group messages use the JID. If it errors due to ffmpeg not being installed, use send_file instead.

        Args:
            recipient (string): The recipient - either a phone number with country code but no + or other symbols,
                             or a JID (e.g., "123456789@s.whatsapp.net" or a group JID like "123456789@g.us")
            media_path (string): The absolute path to the audio file to send (will be converted to Opus .ogg if it's not a .ogg file)
            user_id (string): The user ID to send audio from (default: "default_user")

        Returns:
            Dict[str, Any]: A dictionary containing success status and a status message

        Raises:
            ValueError: Raised when required parameters are missing.

        Tags:
            whatsapp.send_audio_message, important
        """
        if recipient is None:
            raise ValueError("Missing required parameter 'recipient'.")
        if media_path is None:
            raise ValueError("Missing required parameter 'media_path'.")
        success, status_message = whatsapp_audio_voice_message(recipient, media_path, user_id)
        return {
            "success": success,
            "message": status_message,
        }

    def download_media(
        self,
        message_id: str,
        chat_jid: str,
        user_id: str = "default_user",
    ) -> Dict[str, Any]:
        """
        Download media from a WhatsApp message and get the local file path.

        Args:
            message_id (string): The ID of the message containing the media
            chat_jid (string): The JID of the chat containing the message
            user_id (string): The user ID to download media for (default: "default_user")

        Returns:
            Dict[str, Any]: A dictionary containing success status, a status message, and the file path if successful

        Raises:
            ValueError: Raised when required parameters are missing.

        Tags:
            whatsapp.download_media, important
        """
        if message_id is None:
            raise ValueError("Missing required parameter 'message_id'.")
        if chat_jid is None:
            raise ValueError("Missing required parameter 'chat_jid'.")
        file_path = whatsapp_download_media(message_id, chat_jid, user_id)
        
        if file_path:
            return {
                "success": True,
                "message": "Media downloaded successfully",
                "file_path": file_path,
            }
        else:
            return {
                "success": False,
                "message": "Failed to download media",
            }

    def list_tools(self):
        """
        Lists the available tools (methods) for this application.
        """
        return [
            self.search_contacts,
            self.list_messages,
            self.list_chats,
            self.get_chat,
            self.get_direct_chat_by_contact,
            self.get_contact_chats,
            self.get_last_interaction,
            self.get_message_context,
            self.send_message,
            self.send_file,
            self.send_audio_message,
            self.download_media,
        ]
