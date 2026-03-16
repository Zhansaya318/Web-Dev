import {Routes} from '@angular/router';

// import {Home} from './home/home';
// import {User} from './user/user';

export const routes: Routes = [
  {
    path: '',
    title: 'App Home Page',
    // component: Home,
  },
  {
    path: 'user',
    title: 'App User Page',
    // component: User,
  },
];

// import {Component} from '@angular/core';
//
// @Component({
//   selector: 'app-home',
//   template: ` <div>Home Page</div> `,
// })
// export class Home {}
//

// import {Component} from '@angular/core';
//
// @Component({
//   selector: 'app-user',
//   template: ` <div>Username: {{ username }}</div> `,
// })
// export class User {
//   username = 'youngTech';
// }
