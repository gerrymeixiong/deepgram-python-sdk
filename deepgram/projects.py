from ._types import Options, Project, ProjectResponse
from ._utils import _request

class Projects:
    _root = "/v1/projects";

    def __init__(self, options: Options) -> None:
        self.options = options

    async def list(self) -> ProjectResponse:
        """Returns all projects accessible by the API key."""
        return await _request(self._root, self.options)

    async def get(self, id: str) -> Project:
        """Retrieves a specific project based on the provided projectId."""
        return await _request(f'{self._root}/{id}', self.options)

    # These endpoints are not yet programatically accessible.

    # async def create(self, name: str) -> Project:
    # 	"""Creates a project."""
    # 	return await _request(self._root, self.options, method='POST', payload={'name': name})