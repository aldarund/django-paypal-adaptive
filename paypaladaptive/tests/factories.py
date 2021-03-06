import datetime

import factory
import uuid

from moneyed import Money

from paypaladaptive.models import Payment, Preapproval, PaypalAdaptive


class PaypalAdaptiveFactory(factory.DjangoModelFactory):
    FACTORY_FOR = PaypalAdaptive

    money = Money(1400, 'SEK')
    money_currency = 'SEK'
    created_date = datetime.datetime.now()


class PaymentFactory(PaypalAdaptiveFactory):
    FACTORY_FOR = Payment
    # transaction_id = str(uuid.uuid4())[0:17]


class PreapprovalFactory(PaypalAdaptiveFactory):
    FACTORY_FOR = Preapproval
