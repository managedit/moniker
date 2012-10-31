# Copyright 2012 Managed I.T.
#
# Author: Kiall Mac Innes <kiall@managedit.ie>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import abc
from moniker.openstack.common import log as logging


LOG = logging.getLogger(__name__)


class Handler(object):
    """ Base class for notification handlers """

    __metaclass__ = abc.ABCMeta

    def __init__(self, storage_conn, *args, **kwargs):
        LOG.debug('Loaded handler: %s' % __name__)
        self.storage_conn = storage_conn

    @abc.abstractmethod
    def get_notification_types(self):
        """ Returns a list of notification types this class can process """

    @abc.abstractmethod
    def process_notification(self, notification):
        """ Processes a given notification """
