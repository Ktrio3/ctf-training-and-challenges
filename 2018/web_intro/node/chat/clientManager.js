var helper = require('./helper')
var exports = module.exports = {
    clients: {},
    getUserByClient: function(client) {
        return this.clients[client.id]
    },
    registerClient: function (client, user) {
        this.clients[client.id] = { 'c': client,
                                    'u': user,
                                    'ch': {}
        };
    },
    removeClient: function (client) {
        var client_old = this.clients[client.id]
        if(client_old === undefined)
            return client_old

        delete client_old.c
        client_old = helper.clone(client_old)
        delete this.clients[client.id];
        return client_old
    },
    isUserAvailable: function (userName) {
        for (var a of Object.entries(this.clients)) {
          a = a[1]
          if(a.u.name == userName) {
            return false;
          }
        }
        return true;
    },
    getUsername: function (client) {
        return this.clients[client.id].u.name;
    },
    getLastname: function (client) {
        return this.clients[client.id].u.lastname;
    },
    getCountry: function (client) {
        return this.clients[client.id].u.country;
    },
    getLocation: function (client) {
        return this.clients[client.id].u.location;
    },
    getStatus: function (client) {
        return this.clients[client.id].u.status;
    },
    joinChannel: function (client, channel) {
        this.clients[client.id].ch[channel] = true;
    },
    leaveChannel: function (client, channel) {
        this.clients[client.id].ch[channel] = false;
    },
    getSubscribedToChannel: function(channel) {
        var subscribed = [];
        for (var a of Object.entries(this.clients)) {
            a = a[1]
            if(a.ch[channel] === true) {
                subscribed.push(a.c);
            }
        }
        return subscribed;
    },
    isSubscribedTo: function(client, channel) {
        var user = this.getUserByClient(client)

        for (var a of Object.entries(user.ch)) {
            if(a.state === true && a.chs === channel) {
                return true;
            }
        }

        return false;
    },
};
