"""The transaction related models and enums."""
from datetime import datetime
from enum import Enum
import typing


from privacy.schema.base import CustomBase
from privacy.schema.card import Card
from privacy.schema.event import Event, Results
from privacy.schema.funding import Account
from privacy.schema.merchant import Merchant


class Statuses(Enum):
    """An enum of the transaction statuses"""
    PENDING = "PENDING"
    VOIDED = "VOIDED"
    SETTLING = "SETTLING"
    SETTLED = "SETTLED"
    BOUNCED = "BOUNCED"


class Transaction(CustomBase):
    """
    The Transaction Model

    Attributes:
        amount (int): The authorization  amount of the transaction (in pennies).
        card (privacy.schema.card.Card): The card tied to this transaction.
        created (datetime.datetime): The datetime of when this transaction first occurred.
        events (list[ privacy.schema.event.Event ], premium): the events that have modified this.
        funding (list[ privacy.schema.funding.Account ]): All the founding sources.
        merchant (privacy.schema.merchant.Merchant): The merchant tied to this transaction.
        result (privacy.schema.event.Results): The result of this transaction.
        settled_amount (int): The amount of that has been settled (in pennies) (may change).
        status (privacy.schema.transaction.Statuses): The status of this transaction.
        token (int): The globally unique identifier for this transaction.
    """
    amount: int
    card: Card
    created: datetime
    events: typing.List[Event]
    funding: typing.List[Account]
    merchant: Merchant
    result: Results
    settled_amount: int
    status: Statuses
    token: str

    def __repr__(self):
        return f"<Transaction({self.token}:{self.status})>"
