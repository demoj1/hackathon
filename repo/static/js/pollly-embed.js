'use strict';

var embeds = document.getElementsByClassName('pollly-embed');

if(embeds) {

    for(var i = 0; i < embeds.length; i++) {

        var id = embeds[i].getAttribute('data-id');
        embeds[i].innerHTML = '<iframe id="pollly-iframe-' + id + '" style="border:0;width:100%" src="http://poll.ly/#/' + id + '/iframe"></iframe>';

    }

    window.addEventListener('message', function(e) {

        var eventName = e.data[0];
        var data = e.data[1];
        switch(eventName) {

            case 'embedHeight.'+id:
                document.getElementById('pollly-iframe-'+id).style.height = data + 'px';
                break;

        }

    });
}