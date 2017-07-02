from pygame import transform

from pgzero.actor import Actor

class Actor2(Actor):
    def __init__(self, *args, **kwargs):
        super(Actor2, self).__init__(*args, **kwargs)
        self._angle = 0.0
        self._orig_surf = self._surf

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, angle):
        self._angle = angle
        pos = self.pos
        self._surf = transform.rotate(self._orig_surf, angle)
        self.width, self.height = self._surf.get_size()
        self._calc_anchor()
        self.pos = pos