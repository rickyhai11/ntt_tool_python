nttApp.service('trafficService', function(dataService){
    this.list = function(cloudId){
        return dataService.get('/api/traffic/?cloud_id=' + cloudId);
    };

    this.get = function(pk) {
        return dataService.get('/api/traffic/' + pk + '/');
    };

    this.create = function(params){
        return dataService.post('/api/traffic/', params);
    };

    this.update = function(pk, params){
        return dataService.put('/api/traffic/'+pk+'/', params);
    };

    this.delete = function(pk){
        return dataService.delete('/api/traffic/'+pk+'/');
    };

    this.selectTenant = function(pk, tenant_id){
        return dataService.get('/api/traffic/' + pk + '/select/tenant/' + tenant_id + '/');
    };

    this.selectNetwork = function(pk, params){
        return dataService.get('/api/traffic/' + pk + '/select/network/?'+$.param(params));
    };

    this.discoverEndpoints = function(pk, params){
        return dataService.postJSON('/api/traffic/' +pk + '/endpoints/discover/', $.param(params))
    };
1
    this.launchVM = function(pk){
        return dataService.get('/api/traffic/' + pk + '/vm/launch/');
    };

    this.test = function(pk){
        return dataService.get('/api/traffic/' + pk + '/test/');
    };
});






