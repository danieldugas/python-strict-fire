# Copyright (C) 2018 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests importing the strictfire module."""

import sys

import strictfire
from strictfire import testutils
import mock


class FireImportTest(testutils.BaseTestCase):
  """Tests importing Fire."""

  def testFire(self):
    with mock.patch.object(sys, 'argv', ['commandname']):
      strictfire.StrictFire()

  def testFireMethods(self):
    self.assertIsNotNone(strictfire.StrictFire)

  def testNoPrivateMethods(self):
    self.assertTrue(hasattr(strictfire, 'StrictFire'))
    self.assertFalse(hasattr(strictfire, '_Fire'))


if __name__ == '__main__':
  testutils.main()
