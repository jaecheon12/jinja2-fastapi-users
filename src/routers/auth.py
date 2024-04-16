from fastapi_users import FastAPIUsers

# bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

# def get_jwt_strategy() -> JWTStrategy:
#     return JWTStrategy(secret=config["SECRET"], lifetime_seconds=3600)


# google_oauth_client = GoogleOAuth2(
#     os.getenv(config["GOOGLE_OAUTH_CLIENT_ID"], ""),
#     os.getenv(config["GOOGLE_OAUTH_CLIENT_SECRET"], ""),
# )

# class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
#     reset_password_token_secret = config["SECRET"]
#     verification_token_secret = config["SECRET"]

#     async def on_after_register(self, user: User, request: Optional[Request] = None):
#         print(f"User {user.id} has registered.")

#     async def on_after_forgot_password(
#         self, user: User, token: str, request: Optional[Request] = None
#     ):
#         print(f"User {user.id} has forgot their password. Reset token: {token}")

#     async def on_after_request_verify(
#         self, user: User, token: str, request: Optional[Request] = None
#     ):
#         print(f"Verification requested for user {user.id}. Verification token: {token}")

# async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
#     yield UserManager(user_db)


# auth_backend = AuthenticationBackend(
#     name="jwt",
#     transport=bearer_transport,
#     get_strategy=get_jwt_strategy,
# )

fastapi_users = FastAPIUsers()

# current_active_user = fastapi_users.current_user(active=True)