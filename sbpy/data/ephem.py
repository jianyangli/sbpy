# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
======================
SBPy data.Ephem Module
======================

Class for storing and querying ephemerides

created on June 04, 2017
"""


from .core import DataClass

__all__ = ['Ephem']


class Ephem(DataClass):
    """Class for storing and querying ephemerides

<<<<<<< HEAD
    The `Ephem` class provides an interface to
    `PyEphem <http://rhodesmill.org/pyephem/>`_ for ephemeris calculations.
=======
    The `Ephem` class provides an interface to PyEphem
    (http://rhodesmill.org/pyephem/) for ephemeris calculations.
>>>>>>> adef0b2e12cb7086bace482c594d4bfd07a9d514

    """

    @classmethod
    def from_horizons(cls, targetid, id_type='smallbody',
                      epochs=None, observatory='500', **kwargs):
        """
        Load target ephemerides from
        `JPL Horizons <https://ssd.jpl.nasa.gov/horizons.cgi>`_ using
        `astroquery.jplhorizons <http://astroquery.readthedocs.io/en/latest/jplhorizons/jplhorizons.html>`_.

        Parameters
        ----------
        targetid: str, mandatory
            Target identifier.
        id_type: str, optional, default: `'smallbody'`
            the nature of the `targetid` provided; possible values are
            `'smallbody'` (asteroid or comet), `'majorbody'` (planet or
            satellite), `'designation'` (asteroid or comet designation),
            `'name'` (asteroid or comet name), `'asteroid_name'`,
            `'comet_name'`, `'id'` (Horizons id)
        epochs: `astropy.Time` instance or iterable or dictionary, optional, default: None
            Epoch of elements; a list or array of `astropy.Time` objects
            should be used for a number of discrete epochs; a dictionary
            including keywords `start`, `step`, and `stop` can be used to
            generate a range of epochs(see the
            `astroquery.jplhorizons < http: // astroquery.readthedocs.io/en/latest/jplhorizons/jplhorizons.html  # overview>`
            documentation for details); if None is provided, current date
            and time are used.
        observatory: str, optional, default '500' (geocentric)
            location of observer
        **kwargs: optional arguments that will be provided to `~astroquery.jplhorizons.Horizons.ephemerides`

        Returns
        -------
        `~DataClass` object

        Examples
        --------
        >> > from sbpy.data import Ephem
        >> > from astropy.time import Time
        >> > epoch = Time('2018-05-14', scale='utc')
        >> > eph = Ephem.from_horizons('ceres', epochs=epoch)

        """

        from astropy.time import Time

        from astroquery.jplhorizons import Horizons
        from .. import bib

        if epochs is None:
            epochs = [Time.now().jd]
        elif isinstance(epochs, Time):
            epochs = [Time(epochs).jd]

        # load ephemerides using astroquery.jplhorizons
        obj = Horizons(id=targetid, id_type=id_type, location=observatory,
                       epochs=epochs)
        eph = obj.ephemerides(**kwargs)

        return cls.from_table(eph)

    @classmethod
    def from_mpc(cls, targetid, epoch, observatory='500', bib=None):
        """Load ephemerides from the Minor Planet Center(http: // minorplanetcenter.net/).

        Parameters
        ----------
        targetid: str, mandatory
            target identifier
        epochs: astropy Time instance or iterable, optional, default None
            epoch of elements; if None is provided, current date is used
        observatory: str, optional, default '500' (geocentric)
            location of observer
        bib: SBPy Bibliography instance, optional, default None
            Bibliography instance that will be populated

        Returns
        -------
        Astropy Table

        Examples
        --------
        >> > from sbpy.data import Ephem  # doctest: +SKIP
        >> > from astropy.time import Time  # doctest: +SKIP
        >> > epoch = Time('2018-05-14', scale='utc')  # doctest: +SKIP
        >> > eph = Ephem.from_mpc('ceres', '568', epoch)  # doctest: +SKIP

        not yet implemented

        """

    def report_to_mpc(bib=None):
        """Format as a report to the Minor Planet Center
        (http: // minorplanetcenter.net/).

        Parameters
        ----------
        bib: SBPy Bibliography instance, optional, default None
            Bibliography instance that will be populated

        additional parameters will be identified in the future

        Returns
        -------
        str

        Examples
        --------
        >> > from sbpy.data import Ephem  # doctest: +SKIP
        >> > eph = Ephem.from_array...  # doctest: +SKIP
        >> > report = eph.report_to_mpc()  # doctest: +SKIP

        not yet implemented

        """

    @classmethod
    def from_imcce(cls, targetid, epoch, observatory='500', bib=None):
        """Load orbital elements from IMCCE(http: // vo.imcce.fr/webservices/miriade/).

        Parameters
        ----------
        targetid: str, mandatory
            target identifier
        epochs: astropy Time instance or iterable, optional, default None
            epoch of elements; if None is provided, current date is used
        observatory: str, optional, default '500' (geocentric)
            location of observer
        bib: SBPy Bibliography instance, optional, default None
            Bibliography instance that will be populated

        Returns
        -------
        Astropy Table

        Examples
        --------
        >> > from sbpy.data import Ephem  # doctest: +SKIP
        >> > from astropy.time import Time  # doctest: +SKIP
        >> > epoch = Time('2018-05-14', scale='utc')  # doctest: +SKIP
        >> > eph = Ephem.from_imcce('ceres', '568', epoch)  # doctest: +SKIP

        not yet implemented

        """

    @classmethod
    def from_lowell(cls, targetid, epoch, observatory='500', bib=None):
        """Load orbital elements from Lowell Observatory(http: // asteroid.lowell.edu/).

        Parameters
        ----------
        targetid: str, mandatory
            target identifier
        epochs: astropy Time instance or iterable, optional, default None
            epoch of elements; if None is provided, current date is used
        observatory: str, optional, default '500' (geocentric)
            location of observer
        bib: SBPy Bibliography instance, optional, default None
            Bibliography instance that will be populated

        Returns
        -------
        Astropy Table

        Examples
        --------
        >> > from sbpy.data import Ephem  # doctest: +SKIP
        >> > from astropy.time import Time  # doctest: +SKIP
        >> > epoch = Time('2018-05-14', scale='utc')  # doctest: +SKIP
        >> > eph = Ephem.from_lowell('ceres', '568', epoch)  # doctest: +SKIP

        not yet implemented

        """

    @classmethod
    def from_pyephem(cls, orb, location, epoch):
        """Function that derives ephemerides based on an `Astropy.table`
        containing orbital elements using PyEphem(http: // rhodesmill.org/pyephem/).

        Parameters
        ----------
        orb: `Astropy.table`, mandatory
            complete set of orbital elements
        location: str or dictionary, mandatory
            name of location or a dictionary fully describing the location
        epoch: `Astropy.time` object

        Examples
        --------
        >> > from sbpy.data import Ephem, Orbit  # doctest: +SKIP
        >> > orb = Orbit.from_...  # doctest: +SKIP
        >> > eph = Ephem.from_pyephem(orb,  # doctest: +SKIP
        >> >                          location={'name': 'Flagstaff',  # doctest: +SKIP
        >> >                                    'geolon': 35.199167,  # doctest: +SKIP
        >> >                                    'geolat': -111.631111,  # doctest: +SKIP
        >> >                                    'altitude': '2106'},  # doctest: +SKIP
        >> >                          epoch=epoch)  # doctest: +SKIP

        not yet implemented

        """
