// urlB64ToUint8Array is a magic function that will encode the base64 public key
// to Array buffer which is needed by the subscription option
const urlB64ToUint8Array = base64String => {
    const padding = '='.repeat((4 - (base64String.length % 4)) % 4)
    const base64 = (base64String + padding).replace(/\-/g, '+').replace(/_/g, '/')
    const rawData = atob(base64)
    const outputArray = new Uint8Array(rawData.length)
    for (let i = 0; i < rawData.length; ++i) {
      outputArray[i] = rawData.charCodeAt(i)
    }
    return outputArray
  }

  const saveSubscription = async subscription => {
    const SERVER_URL = 'http://localhost:4000/save-subscription'
    const response = await fetch(SERVER_URL, {
      method: 'post',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(subscription),
    })
    return response.json()
  }
  self.addEventListener('activate', async () => {
    // This will be called only once when the service worker is installed for first time.
    try {
      const applicationServerKey = urlB64ToUint8Array(
        'BJ5IxJBWdeqFDJTvrZ4wNRu7UY2XigDXjgiUBYEYVXDudxhEs0ReOJRBcBHsPYgZ5dyV8VjyqzbQKS8V7bUAglk'
      )
      const options = { applicationServerKey, userVisibleOnly: true }
      const subscription = await self.registration.pushManager.subscribe(options)
      const response = await saveSubscription(subscription)
      console.log(response)
    } catch (err) {
      console.log('Error', err)
    }
  })
  self.addEventListener('push', function(event) {
    if (event.data) {
      console.log('Push event!! ', event.data.text())
      showLocalNotification('Yolo', event.data.text(), self.registration)
      
    } else {
      console.log('Push event but no data')
    }
  })
  const showLocalNotification = (title, body, swRegistration) => {
    const options = {
      body,
      // here you can add more properties like icon, image, vibrate, etc.
    }
    var notification = swRegistration.showNotification(title, options)
    
  };
  
  // self.swRegistration.onnotificationclick = function(event) {
  //   console.log('On notification click: ', event.notification.tag);
  //   event.notification.close();
  
  //   // This looks to see if the current is already open and
  //   // focuses if it is
  //   event.waitUntil(clients.matchAll({
  //     type: "window"
  //   }).then(function(clientList) {
  //     for (var i = 0; i < clientList.length; i++) {
  //       var client = clientList[i];
  //       if (client.url == '/' && 'focus' in client)
  //         return client.focus();
  //     }
  //     if (clients.openWindow)
  //       return clients.openWindow('/');
  //   }));
  // };