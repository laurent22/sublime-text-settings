import sublime_plugin, os
 
class RemoteEdit(sublime_plugin.EventListener):
    def on_post_save(self, view):
        remote = { "/opt/lampp/htdocs/tlscontact": "/usr/bin/scp -P 13333 '$1' laurent.cozic@10.90.0.202:'/home/apache/lco/tlscontact/$2'" }
        for dirname, target in remote.iteritems():
            if view.file_name().startswith( dirname ):
                target = target.replace( "$1", view.file_name() )
                target = target.replace( "$2", view.file_name()[len(dirname):] )
                print target
                os.system( target + " &" )
