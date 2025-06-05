import { useState, useEffect, useCallback } from 'react';
import { getCompanyDetails } from '../services/companyService';

/**
 * Custom hook for fetching company details
 * 
 * @param {string} regNumber - Company registration number
 * @returns {Object} The company details state and functions
 */
const useCompanyDetails = (regNumber) => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [company, setCompany] = useState(null);

  const fetchCompanyDetails = useCallback(async () => {
    if (!regNumber) {
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      const data = await getCompanyDetails(regNumber);
      setCompany(data);
    } catch (err) {
      setError(err.message || 'An error occurred while fetching company details');
      console.error('Error fetching company details:', err);
    } finally {
      setIsLoading(false);
    }
  }, [regNumber]);

  useEffect(() => {
    fetchCompanyDetails();
  }, [fetchCompanyDetails]);

  return {
    isLoading,
    error,
    company,
    refetch: fetchCompanyDetails
  };
};

export default useCompanyDetails; 