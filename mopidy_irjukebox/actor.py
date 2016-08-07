from __future__ import unicode_literals

import logging

from mopidy import backend

#from .library import SoundCloudLibraryProvider
#from .soundcloud import SoundCloudClient


logger = logging.getLogger(__name__)


class IrJukeboxBackend(pykka.ThreadingActor, backend.Backend):

    def __init__(self, config, audio):
        super(IrJukeboxBackend, self).__init__()
        self.config = config
        #self.remote = SoundCloudClient(config['soundcloud'])
        #self.library = SoundCloudLibraryProvider(backend=self)
        self.playback = IrJukeboxPlaybackProvider(audio=audio, backend=self)

        self.uri_schemes = ['irjukebox', 'sc']


class IrJukeboxPlaybackProvider(backend.PlaybackProvider):

    def translate_uri(self, uri):
        track_id = self.backend.remote.parse_track_uri(uri)
        track = self.backend.remote.get_track(track_id, True)
        if track is None:
            return None
        return track.uri
