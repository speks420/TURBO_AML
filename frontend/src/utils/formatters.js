/**
 * Format a date string to a more readable format
 * 
 * @param {string} dateString - The date string to format
 * @returns {string} The formatted date
 */
export const formatDate = (dateString) => {
  if (!dateString) return 'Not available';
  
  try {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-GB', {
      day: 'numeric',
      month: 'long',
      year: 'numeric'
    });
  } catch (error) {
    console.error('Error formatting date:', error);
    return dateString;
  }
};

/**
 * Format a company status string to a more standardized format
 * 
 * @param {string} status - The company status
 * @returns {string} The formatted status
 */
export const formatStatus = (status) => {
  if (!status) return 'Unknown';
  
  const statusMap = {
    'active': 'Active',
    'liquidated': 'Liquidated',
    'suspended': 'Suspended',
    'bankrupt': 'Bankrupt',
    'closed': 'Closed'
  };
  
  const lowerStatus = status.toLowerCase();
  return statusMap[lowerStatus] || status;
};

/**
 * Format a registration number for display
 * 
 * @param {string} regNumber - The registration number
 * @returns {string} The formatted registration number
 */
export const formatRegNumber = (regNumber) => {
  if (!regNumber) return 'Not available';
  
  // This is a placeholder implementation - 
  // actual formatting would depend on the format of Latvian company registration numbers
  return regNumber.toString().replace(/(\d{6})(\d{5})/, '$1-$2');
}; 