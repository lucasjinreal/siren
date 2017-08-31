# -*- coding: utf-8 -*-
# file: alice.py
# author: JinTian
# time: 29/08/2017 4:39 PM
# Copyright 2017 JinTian. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------
import paho.mqtt.client as mqtt
import json
from threading import Thread
import time


def on_connect(client_, user_data, flags, rc):
    print('Alice online...')
    print('connected with result: ' + str(rc))
    client_.subscribe('test/talk')


def on_message(client, userdata, message):
    print("msg: ", str(message.payload.decode("utf-8")))


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect("127.0.0.1", 1883, 60)

        t = Thread(target=client.loop_forever)
        t.setDaemon(True)
        t.start()

        while True:
            time.sleep(2)
            pd = input('you: ')
            client.publish('test/talk', pd)
    except KeyboardInterrupt:
        client.disconnect()
        exit(0)
