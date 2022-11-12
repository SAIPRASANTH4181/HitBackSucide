import { Injectable } from '@angular/core';
import {
  AngularFireAuth
} from '@angular/fire/compat/auth';
import { concatMap, from, Observable, of, switchMap } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  
  constructor(private auth: AngularFireAuth) {}

  signUp(email: string, password: string) {
    return from(this.auth.createUserWithEmailAndPassword(email, password));
  //   this.auth.createUserWithEmailAndPassword( email, password)
  // .then((userCredential) => {
  //   // Signed in 
  //   const user = userCredential.user;
  //   // ...
  // })
  // .catch((error) => {
  //   const errorCode = error.code;
  //   const errorMessage = error.message;
  //   // ..
  // });
  }

  login(email: string, password: string) {
    return from(this.auth.signInWithEmailAndPassword(email, password));
  }

  // updateProfile(profileData: Partial<UserInfo>): Observable<any> {
  //   const user = this.auth.currentUser;
  //   return of(user).pipe(
  //     concatMap((user) => {
  //       if (!user) throw new Error('Not authenticated');

  //       return updateProfile(user, profileData);
  //     })
  //   );
  // }

  logout(): Observable<any> {
    return from(this.auth.signOut());
  }
}
