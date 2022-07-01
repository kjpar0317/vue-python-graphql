# async def load_codeProblems_by_code(keys: list) -> list[CodeProblem]:
#     async with models.get_session() as s:
#         all_queries = [select(CodeM).where(
#             CodeM.C_ID == key) for key in keys]
#         print(all_queries)
#         data = [(await s.execute(sql)).scalars().unique().all() for sql in all_queries]
#         print(keys, data)
#     return data


# async def get_context() -> dict:
#     return {
#         "codeProblems_by_code": DataLoader(load_fn=load_codeProblems_by_code),
# }
