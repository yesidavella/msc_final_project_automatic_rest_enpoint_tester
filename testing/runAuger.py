import auger

from testing import Foo

with auger.magic([Foo]):
    Foo.main()