import grok, os

from zope.app.authentication.authentication import PluggableAuthentication
from zope.app.security.interfaces import IAuthentication

from hurry.query.query import Query
from hurry.query.interfaces import IQuery

from raptus.mailcone.auth.auth import setup_authentication
from raptus.mailcone.cronjob.contents import CronJobContainer

from raptus.mailcone.core.interfaces import IMailcone


class Mailcone(grok.Application, grok.Container):
    grok.implements(IMailcone)
    grok.local_utility(PluggableAuthentication, provides=IAuthentication, setup=setup_authentication)
    grok.local_utility(Query, provides=IQuery)
    grok.local_utility(CronJobContainer, name_in_container='cronjobs', public=True)
