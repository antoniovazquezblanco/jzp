#!/usr/bin/env python

from abc import ABC
from struct import unpack


class InvalidFileMagicException(Exception):
    def __init__(self, message="Invalid file magic!") -> None:
        super().__init__(message)


class JzpHeader(ABC):
    def __init__(self, revision, comp_size, decomp_size, offset_width, size_width, size_min, content_offset) -> None:
        self.revision = revision
        self.comp_size = comp_size
        self.decomp_size = decomp_size
        self.offset_width = offset_width
        self.size_width = size_width
        self.size_min = size_min
        self.content_offset = content_offset


class JazipHeader(JzpHeader):
    def __init__(self, data) -> None:
        if len(data) < 36:
            raise Exception('Not enough data')
        magic = data[26:32]
        if magic != b'JAZIP\x00':
            raise InvalidFileMagicException
        revision = data[0:18]
        decomp_size = unpack('>I', data[18:22])[0]
        comp_size = unpack('>I', data[22:26])[0]
        offset_width = data[32]
        size_info = data[33]
        size_width = size_info >> 4
        size_min = size_info & 0xf
        super().__init__(revision, comp_size, decomp_size, offset_width, size_width, size_min, 36)


class AgltzipHeader(JzpHeader):
    def __init__(self, data) -> None:
        if len(data) < 156:
            raise Exception('Not enough data')
        magic = data[144:152]
        if magic != b'AGLTZIP\x00':
            raise InvalidFileMagicException
        revision = data[0:128]
        comp_size = unpack('>I', data[128:132])[0]
        #comp_checksum = unpack('>I', data[132:136])
        decomp_size = unpack('>I', data[136:140])[0]
        #decomp_checksum = unpack('>I', data[140:144])
        offset_width = data[152]
        size_info = data[153]
        size_width = size_info >> 4
        size_min = size_info & 0xf
        super().__init__(revision, comp_size, decomp_size, offset_width, size_width, size_min, 156)


def header_parse(data):
    try:
        return JazipHeader(data=data)
    except InvalidFileMagicException:
        pass
    try:
        return AgltzipHeader(data=data)
    except InvalidFileMagicException:
        pass
    return None
