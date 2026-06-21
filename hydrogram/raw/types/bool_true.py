#  Hydrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2023-present Hydrogram <https://hydrogram.org>
#
#  This file is part of Hydrogram.
#
#  Hydrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Hydrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Hydrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from hydrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hydrogram.raw.core import TLObject
from hydrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class BoolTrue(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~hydrogram.raw.base.Bool`.

    Details:
        - Layer: ``227``
        - ID: ``997275B5``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 213 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contest.SaveDeveloperInfo
            auth.ResetAuthorizations
            auth.BindTempAuthKey
            auth.CancelCode
            auth.DropTempAuthKeys
            auth.CheckRecoveryPassword
            auth.RequestFirebaseSms
            auth.ReportMissingCode
            account.RegisterDevice
            account.UnregisterDevice
            account.UpdateNotifySettings
            account.ResetNotifySettings
            account.UpdateStatus
            account.ReportPeer
            account.CheckUsername
            account.DeleteAccount
            account.SetAccountTTL
            account.UpdateDeviceLocked
            account.ResetAuthorization
            account.UpdatePasswordSettings
            account.ConfirmPhone
            account.ResetWebAuthorization
            account.ResetWebAuthorizations
            account.DeleteSecureValue
            account.AcceptAuthorization
            account.VerifyPhone
            account.FinishTakeoutSession
            account.ConfirmPasswordEmail
            account.ResendPasswordEmail
            account.CancelPasswordEmail
            account.GetContactSignUpNotification
            account.SetContactSignUpNotification
            account.SaveWallPaper
            account.InstallWallPaper
            account.ResetWallPapers
            account.SaveAutoDownloadSettings
            account.SaveTheme
            account.InstallTheme
            account.SetContentSettings
            account.ReportProfilePhoto
            account.DeclinePasswordReset
            account.SetAuthorizationTTL
            account.ChangeAuthorizationSettings
            account.UpdateEmojiStatus
            account.ClearRecentEmojiStatuses
            account.ReorderUsernames
            account.ToggleUsername
            account.SaveAutoSaveSettings
            account.DeleteAutoSaveExceptions
            account.InvalidateSignInCodes
            account.UpdateColor
            account.UpdateBusinessWorkHours
            account.UpdateBusinessLocation
            account.UpdateBusinessGreetingMessage
            account.UpdateBusinessAwayMessage
            account.UpdateBusinessIntro
            account.ToggleConnectedBotPaused
            account.DisablePeerConnectedBot
            account.UpdateBirthday
            account.DeleteBusinessChatLink
            account.UpdatePersonalChannel
            account.ToggleSponsoredMessages
            account.ToggleNoPaidMessagesException
            account.SetMainProfileTab
            account.SaveMusic
            account.DeletePasskey
            account.ConfirmBotConnection
            users.SetSecureValueErrors
            contacts.DeleteByPhones
            contacts.Block
            contacts.Unblock
            contacts.ResetTopPeerRating
            contacts.ResetSaved
            contacts.ToggleTopPeers
            contacts.EditCloseFriends
            contacts.SetBlocked
            contacts.UpdateContactNote
            messages.SetTyping
            messages.ReportSpam
            messages.DiscardEncryption
            messages.SetEncryptedTyping
            messages.ReadEncryptedHistory
            messages.ReportEncryptedSpam
            messages.UninstallStickerSet
            messages.EditChatAdmin
            messages.ReorderStickerSets
            messages.SaveGif
            messages.SetInlineBotResults
            messages.EditInlineBotMessage
            messages.SetBotCallbackAnswer
            messages.SaveDraft
            messages.ReadFeaturedStickers
            messages.SaveRecentSticker
            messages.ClearRecentStickers
            messages.SetInlineGameScore
            messages.ToggleDialogPin
            messages.ReorderPinnedDialogs
            messages.SetBotShippingResults
            messages.SetBotPrecheckoutResults
            messages.FaveSticker
            messages.MarkDialogUnread
            messages.ClearAllDrafts
            messages.EditChatAbout
            messages.HidePeerSettingsBar
            messages.ToggleStickerSets
            messages.UpdateDialogFilter
            messages.UpdateDialogFiltersOrder
            messages.ReadDiscussion
            messages.DeleteChat
            messages.StartHistoryImport
            messages.DeleteRevokedExportedChatInvites
            messages.DeleteExportedChatInvite
            messages.SaveDefaultSendAs
            messages.SetDefaultReaction
            messages.ToggleBotInAttachMenu
            messages.ProlongWebView
            messages.RateTranscribedAudio
            messages.ReportReaction
            messages.ClearRecentReactions
            messages.SetDefaultHistoryTTL
            messages.TogglePeerTranslations
            messages.ToggleSavedDialogPin
            messages.ReorderPinnedSavedDialogs
            messages.UpdateSavedReactionTag
            messages.ReorderQuickReplies
            messages.CheckQuickReplyShortcut
            messages.EditQuickReplyShortcut
            messages.DeleteQuickReplyShortcut
            messages.ToggleDialogFilterTags
            messages.TogglePaidReactionPrivacy
            messages.ViewSponsoredMessage
            messages.ClickSponsoredMessage
            messages.ReportMessagesDelivery
            messages.ReadSavedHistory
            messages.DeclineUrlAuth
            messages.CheckUrlAuthMatchCode
            messages.ReportReadMetrics
            messages.ReportMusicListen
            messages.DeleteParticipantReactions
            upload.SaveFilePart
            upload.SaveBigFilePart
            help.SetBotUpdatesStatus
            help.AcceptTermsOfService
            help.SaveAppLog
            help.HidePromoData
            help.DismissSuggestion
            channels.ReadHistory
            channels.ReportSpam
            channels.CheckUsername
            channels.UpdateUsername
            channels.SetStickers
            channels.ReadMessageContents
            channels.SetDiscussionGroup
            channels.EditLocation
            channels.ReorderUsernames
            channels.ToggleUsername
            channels.DeactivateAllUsernames
            channels.ReportAntiSpamFalsePositive
            channels.SetEmojiStickers
            channels.SetMainProfileTab
            bots.AnswerWebhookJSONQuery
            bots.SetBotCommands
            bots.ResetBotCommands
            bots.SetBotMenuButton
            bots.SetBotBroadcastDefaultAdminRights
            bots.SetBotGroupDefaultAdminRights
            bots.SetBotInfo
            bots.ReorderUsernames
            bots.ToggleUsername
            bots.CanSendMessage
            bots.DeletePreviewMedia
            bots.ReorderPreviewMedias
            bots.UpdateUserEmojiStatus
            bots.ToggleUserEmojiStatusPermission
            bots.CheckDownloadFileParams
            bots.SetCustomVerification
            bots.CheckUsername
            bots.EditAccessSettings
            bots.SetJoinChatResults
            payments.ClearSavedInfo
            payments.ChangeStarsSubscription
            payments.FulfillStarsSubscription
            payments.SaveStarGift
            payments.ConvertStarGift
            payments.BotCancelStarsSubscription
            payments.ToggleChatStarGiftNotifications
            payments.ToggleStarGiftsPinnedToTop
            payments.CanPurchaseStore
            payments.ReorderStarGiftCollections
            payments.DeleteStarGiftCollection
            stickers.CheckShortName
            stickers.DeleteStickerSet
            phone.ReceivedCall
            phone.SaveCallDebug
            phone.SendSignalingData
            phone.SaveDefaultGroupCallJoinAs
            phone.SaveCallLog
            phone.SendGroupCallEncryptedMessage
            phone.SaveDefaultSendAs
            chatlists.DeleteExportedInvite
            chatlists.HideChatlistUpdates
            stories.ToggleAllStoriesHidden
            stories.IncrementStoryViews
            stories.TogglePeerStoriesHidden
            stories.TogglePinnedToTop
            stories.ReorderAlbums
            stories.DeleteAlbum
            smsjobs.Join
            smsjobs.Leave
            smsjobs.UpdateSettings
            smsjobs.FinishJob
            aicompose.SaveTone
            aicompose.DeleteTone
    """

    __slots__: List[str] = []

    ID = 0x997275b5
    QUALNAME = "types.BoolTrue"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BoolTrue":
        # No flags
        
        return BoolTrue()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        return b.getvalue()
