#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/26 11:32
# @Author  : 甄超锋

import os


class CutFiles(object):
    def __init__(self):
        self.cut_size = 100 * 1024 * 1024

    def cuttings(self, file: str, cut_size: int, out_dir: str='.'):
        """
        start execute cuttings file!!!
        :param file: file path
        :param cut_size: file split size in bytes, default 100M
        :param out_dir: save file path
        :return:
        """
        if not cut_size:
            cut_size = self.cut_size
        filedir, filename = os.path.split(file)

        filename, extension = os.path.splitext(filename)

        filedir = os.path.join(out_dir, filename)

        if not os.path.exists(filedir):
            os.mkdir(filedir)

        filenum = 0
        stream = open(file, 'rb')

        while True:
            partfilename = os.path.join(filedir, filename + '_' + str(filenum) + extension)
            print('cut log start %s' % partfilename)
            part_stream = open(partfilename, 'wb')

            read_count = 0

            while True:
                read_content = stream.readline()
                if not read_content:
                    print('split done')
                    return
                read_count_per = len(read_content)

                if read_count_per > 0:
                    part_stream.write(read_content)
                else:
                    break

                read_count += read_count_per
                if read_count > cut_size:
                    break

            part_stream.close()
            filenum += 1
