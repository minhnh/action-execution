#!/usr/bin/env python

import rospy

from ae_ros_message_converter.converters.pose_converter import PoseStampedConverter
from ae_ros_message_converter.converters.bbox_converter import BoundingBoxConverter
from ae_ros_message_converter.converters.object_converter import ObjectConverter

class ConverterFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def convert(msg):
        '''Converts 'msg' to an appropriate type if it is a known message;
        returns None otherwise.

        Keyword:
        msg -- a ros message

        '''
        if type(msg).__name__.lower() == 'posestamped':
            return PoseStampedConverter.convert(msg)
        elif type(msg).__name__.lower() == 'boundingbox':
            return BoundingBoxConverter.convert(msg)
        elif type(msg).__name__.lower() == 'object':
            return ObjectConverter.convert(msg)

        rospy.loginfo('[ConverterFactory] Unknown message type; ignoring request')
        return None