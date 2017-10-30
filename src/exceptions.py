class VertexAlreadyConnectedError(Exception):

    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def __str__(self):
        return "%s is already connected to %s" % (self.src, self.dst)


class VertexNotConnectedError(Exception):

    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def __str__(self):
        return "%s is not connected to %s" % (self.src, self.dst)


class VertexAlreadyExists(Exception):

    def __init__(self, vertex):
        self.vertex = vertex

    def __str__(self):
        return "%s is already in graph" % self.vertex


class VertexNotFoundError(Exception):

    def __init__(self, vid):
        self.vid = vid

    def __str__(self):
        return "%s was not found in graph" % self.vid
