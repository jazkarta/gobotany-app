requirejs.config({
    baseUrl: '.',
    paths: {
        'bridge': 'bridge',
        'dkey': 'dkey',
        'lib': 'lib',
        'mapping': 'mapping',
        'markerclusterer': 'lib/markerclusterer_compiled',
        'plantpreview': 'plantpreview',
        'plantshare': 'plantshare',
        'simplekey': 'simplekey',
        'site': 'site',
        'taxa': 'taxa',
        'util': 'util'
    },
    shim: {
        'markerclusterer': {
            exports: "MarkerClusterer"
        }
    }
});
